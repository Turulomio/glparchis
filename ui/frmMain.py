import sys, os, urllib.request,   datetime
if sys.platform=='win32':
    sys.path.append("ui")
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from libglparchis import *

from Ui_frmMain import *
from wdgGame import *
from frmAbout import *
from frmInitGame import *
from frmSettings import *
from frmHelp import *

            
class frmMain(QMainWindow, Ui_frmMain):#    
    def __init__(self, cfgfile, parent = 0,  flags = False):
        QMainWindow.__init__(self)
        self.cfgfile=cfgfile
        self.setupUi(self)
        self.showMaximized()
        self.game=None
        if datetime.date.today()-datetime.date.fromordinal(self.cfgfile.lastupdate)>=datetime.timedelta(days=7):
            print ("Actualizando")
            self.checkUpdates(False)
        self.setWindowTitle(self.tr("glParchis 2010-{}. GNU General Public License \xa9").format(version[0:4]))
        
        #Ajusta el sonido desde cfgfile
        self.cfgfile.sound=not self.cfgfile.sound #Se cambia antes para que self.on_actionSound_triggered lo deje bien
        self.on_actionSound_triggered()
        
    @pyqtSlot()      
    def on_actionAcercaDe_triggered(self):
        fr=frmAbout(self,"frmabout")
        fr.open()
                
    @pyqtSlot()      
    def on_actionHelp_triggered(self):
        fr=frmHelp(self,"frmHelp")
        fr.open()
        
    @pyqtSlot()      
    def on_actionSettings_triggered(self):
        f=frmSettings(self.cfgfile,   self)
        f.exec_()
        if self.game!=None:
            self.game.retranslateUi(self)
            for p in self.game.panels:
                p.retranslateUi(self)
                p.repaint()
                p.setJugador(p.jugador)#Se repinta
        self.retranslateUi(self)
        self.repaint()
        
    @pyqtSlot()      
    def on_actionSound_triggered(self):
        self.cfgfile.sound=not self.cfgfile.sound
        if self.cfgfile.sound:
            self.actionSound.setText(self.tr("Sonido encendido")) 
            icon8 = QtGui.QIcon()
            icon8.addPixmap(QtGui.QPixmap(":/glparchis/sound.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.actionSound.setIcon(icon8)
        else:
            self.actionSound.setText(self.tr("Sonido apagado"))
            icon8 = QtGui.QIcon()
            icon8.addPixmap(QtGui.QPixmap(":/glparchis/soundoff.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.actionSound.setIcon(icon8)
        self.cfgfile.save() ##Cambia los cambios del sound en el cfgfile
        
    @pyqtSlot()      
    def on_actionUpdates_triggered(self):
        self.checkUpdates(True)
        
    def checkUpdates(self, showdialogwhennoupdates=False):
        #Chequea en Internet
        try:
            web=b2s(urllib.request.urlopen('https://sourceforge.net/projects/glparchis/files/glparchis/').read())
        except:
            web=None
        #Si hay error de internet avisa
        if web==None:
            if showdialogwhennoupdates==True:
                m=QMessageBox()
                m.setIcon(QMessageBox.Information)
                m.setText(self.tr("No se ha podido comprobar si hay actualizaciones. Inténtelo más tarde."))
                m.exec_() 
            return
        #Saca la version de internet
        remoteversion=None
        for line in web.split("\n"):
            if line.find('folder warn')!=-1:
                remoteversion=line.split('glparchis-')[1].split('"') [0]
                break
        #Si no hay version sale
        print ("Remote version",  remoteversion)
        if remoteversion==None:
            return
                
        if remoteversion==version.replace("+", ""):#Quita el más de desarrollo 
            if showdialogwhennoupdates==True:
                m=QMessageBox()
                m.setIcon(QMessageBox.Information)
                m.setText(self.tr("Dispone de la última versión del juego"))
                m.exec_() 
        else:
            m=QMessageBox()
            m.setIcon(QMessageBox.Information)
            m.setTextFormat(Qt.RichText)#this is what makes the links clickable
            m.setText(self.tr("Hay una nueva versión del programa. Bájatela de la página web del proyecto <a href='http://glparchis.sourceforge.net'>http://glparchis.sourceforge.net</a> o directamente desde <a href='https://sourceforge.net/projects/glparchis/files/glparchis/glparchis-")+remoteversion+"/'>Sourceforge</a>")
            m.exec_()                 
        self.cfgfile.lastupdate=datetime.date.today().toordinal()
        self.cfgfile.save()
        

        
    @pyqtSlot(QEvent)   
    def closeEvent(self,event):   
        print ("saliendo")
        if self.game:
            self.game.__del__()
        qApp.closeAllWindows()
        qApp.exit()
        sys.exit(0)
  
    def showWdgGame(self):
        self.actionSound.setEnabled(True)
        if self.game!=None:
            self.layout.removeWidget(self.game)    
            self.game.__del__()
        self.game=wdgGame(self)
        self.game.stopthegame=False
        self.layout.addWidget(self.game)
        self.actionGuardarPartida.setEnabled(True)
        self.game.assign_mem(self.mem)
        

    @pyqtSlot()  
    def on_actionRecuperarPartida_triggered(self):
        cwd=os.getcwd()
        os.chdir(os.path.expanduser("~/.glparchis/"))
        #ÐEBE SERLOCAL
        filenam=os.path.basename(QFileDialog.getOpenFileName(self, "", "", "glParchis game (*.glparchis)")[0])
        if filenam!="":
            #Busca si es de 4,6,8
            self.mem=self.selectMem(filenam)
            self.mem.cfgfile=self.cfgfile #Punto a cfgfile
            if self.mem.load(filenam)==False:
                self.mem=None
                return
            for i, j in enumerate(self.mem.jugadores.arr):
                j.name=self.cfgfile.names[i]
            self.showWdgGame()
        os.chdir(cwd)

    def selectMem(self, filename):
        resultado=None
        cwd=os.getcwd()
        os.chdir(os.path.expanduser("~/.glparchis/"))
        config = configparser.ConfigParser()
        config.read(filename)
        try:
            self.maxplayers=int(config.get("game",  "numplayers"))
        except:
            resultado=Mem4()
            os.chdir(cwd)
            return resultado            
        os.chdir(cwd)
            
        if self.maxplayers==4:
            resultado=Mem4()
        elif self.maxplayers==6:
            resultado=Mem6()
        elif self.maxplayers==8:
            resultado=Mem8()
        return resultado



    @pyqtSlot()  
    def on_actionPartidaNueva4_triggered(self):
        self.mem=Mem4()
        self.mem.cfgfile=self.cfgfile
        initgame=frmInitGame(self.mem,  self)
        salida=initgame.exec_()
        if salida==QDialog.Accepted:
            self.showWdgGame()

    @pyqtSlot()  
    def on_actionPartidaNueva6_triggered(self):
        self.mem=Mem6()
        self.mem.cfgfile=self.cfgfile
        initgame=frmInitGame(self.mem,  self)
        salida=initgame.exec_()
        if salida==QDialog.Accepted:
            self.showWdgGame()


    @pyqtSlot()  
    def on_actionPartidaNueva8_triggered(self):
        self.mem=Mem8()
        self.mem.cfgfile=self.cfgfile
        initgame=frmInitGame(self.mem,  self)
        salida=initgame.exec_()
        if salida==QDialog.Accepted:
            self.showWdgGame()


    @pyqtSlot()     
    def on_actionGuardarPartida_triggered(self):
        cwd=os.getcwd()
        os.chdir(os.path.expanduser("~/.glparchis/"))
        filename=os.path.basename(QFileDialog.getSaveFileName(self, "", "", "glParchis game (*.glparchis)"))
        if filename!="":       
            if os.path.splitext(filename)[1]!=".glparchis":
                filename=filename+".glparchis"
            self.mem.save(filename)
        os.chdir(cwd)
