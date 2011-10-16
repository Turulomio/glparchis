## -*- coding: utf-8 -*-
import sys,  random,  ConfigParser,  os
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from xml.dom.minidom import parse
import libglparchis

from Ui_frmMain import *
from frmAbout import *
from wdgUserPanel import *
from wdgGame import *
from frmInitGame import *

class frmMain(QMainWindow, Ui_frmMain):#    
    def __init__(self, parent = 0,  flags = False):
        """
        Constructor
        
        @param parent The parent widget of this dialog. (QWidget)
        @param name The name of this dialog. (QString)
        @param modal Flag indicating a modal dialog. (boolean)
        """
        QMainWindow.__init__(self, None)
        self.setupUi(self)
        self.showMaximized()
        
        self.panel1.setEnabled(False)
        self.panel1.lblAvatar.setPixmap(QtGui.QPixmap(":/glparchis/fichaamarilla.png"))
        self.panel1.show()
        self.panel2.setEnabled(False)
        self.panel2.lblAvatar.setPixmap(QtGui.QPixmap(":/glparchis/fichaazul.png"))
        self.panel2.show()
        self.panel3.setEnabled(False)
        self.panel3.show()
        self.panel4.setEnabled(False)
        self.panel4.lblAvatar.setPixmap(QtGui.QPixmap(":/glparchis/fichaverde.png"))
        self.panel4.show()
        self.logs = []
        self.logs1=[]
        self.logs2=[]
        self.logs3=[]
        self.logs4=[]
        QtCore.QObject.connect(self.ogl, QtCore.SIGNAL('newLog(QString)'), self.lstLog_newLog)  
        QtCore.QObject.connect(self.ogl, QtCore.SIGNAL('cambiar_jugador()'), self.cambiar_jugador)  
        QtCore.QObject.connect(self.ogl, QtCore.SIGNAL('volver_a_tirar()'), self.volver_a_tirar)  
        self.settings_splitter_load()
        

        
        
    def on_splitter_splitterMoved(self, position, index):
        self.settings_splitter_save()
        
    @pyqtSignature("")
    def on_cmdTirarDado_clicked(self):
        self.on_actionDado_activated()
        
    def enable_panel(self, idjugador, bool):
        if idjugador==0:
            self.panel1.setEnabled(bool)
        elif idjugador==1:
            self.panel2.setEnabled(bool)
        elif idjugador==2:
            self.panel3.setEnabled(bool)
        elif idjugador==3:
            self.panel4.setEnabled(bool)    
            
    def lstLog_newLog(self, log):
        if self.ogl.jugadoractual==0:
            panel=self.panel1
            logs=self.logs1
        elif self.ogl.jugadoractual==1:
            panel=self.panel2
            logs=self.logs2
        elif self.ogl.jugadoractual==2:
            panel=self.panel3
            logs=self.logs3
        elif self.ogl.jugadoractual==3:
            panel=self.panel4        
            logs=self.logs4
        logs.append( log)
        panel.lst.setModel(QStringListModel(logs))
        panel.lst.show()


    def settings_splitter_save(self):
        config = ConfigParser.ConfigParser()
        config.read(libglparchis.cfgfile)
        if config.has_section("frmMain")==False:
            config.add_section("frmMain")
        config.set("frmMain",  'splitter_state', self.splitter.saveState())
        with open(libglparchis.cfgfile, 'w') as configfile:
            config.write(configfile)
        
    def settings_splitter_load(self):
        config = ConfigParser.ConfigParser()
        config.read(libglparchis.cfgfile)
        try:
            position=config.get("frmMain", "splitter_state")
            self.splitter.restoreState(position)
        except:
            print ("No hay fichero de configuración")    
    
        
    @pyqtSignature("")
    def on_actionAcercaDe_activated(self):
        fr=frmAbout(self, "frmabout")
        fr.open()
    
    @QtCore.pyqtSlot()      
    def on_actionSalir_activated(self):
        sys.exit()
    
    @QtCore.pyqtSlot()      
    def on_actionDado_activated(self):  
        def labeldado():
            numero=self.ogl.historicodado[0]
            numlbl=len(self.ogl.historicodado)
            #Selecciona el panel
            if self.ogl.jugadoractual==0:
                panel=self.panel1
            elif self.ogl.jugadoractual==1:
                panel=self.panel2
            elif self.ogl.jugadoractual==2:
                panel=self.panel3
            elif self.ogl.jugadoractual==3:
                panel=self.panel4
            #Selecciona el label
            if numlbl==1:
                label=panel.lbl1
            elif numlbl==2:
                label=panel.lbl2
            elif numlbl==3:
                label=panel.lbl3
            ico=libglparchis.icodado(numero)
            self.actionDado.setIcon(ico)
            self.cmdTirarDado.setIcon(ico)   
            pix=libglparchis.pixdado(numero)
            label.setPixmap(pix)
                
        def jugador_tiene_todas_fichas_en_casa():
            for f in self.ogl.fichas:
                if f.jugador==self.ogl.jugadoractual:
                    if f.ruta!=0:
                        return False
            return True
            
#        numero=5
#        numero= int(random.random()*6)+1
        numero= int(random.random()*2)+5
#        self.lstLog_newLog("Ha salido un " + str(numero))        
#        self.ogl.dado=numero
        self.ogl.pendiente=1
        self.ogl.historicodado.insert(0, numero)
        self.actionDado.setEnabled(False)
        self.cmdTirarDado.setEnabled(False)
        labeldado()
        
        print "num"+ str(numero)
        #LOGICA QUE NO REQUIERE LA INTEVENCION DEL USUARIO
        if jugador_tiene_todas_fichas_en_casa()==True:
            if numero <5:
                self.lstLog_newLog(str(numero)+ "No es un 5 y las tienes todas en casa")
                self.cambiar_jugador()
                return
            elif numero==6 and len(self.ogl.historicodado)==3:
                self.lstLog_newLog("No ha salido un 5, y ha sacado 3 seises, ya no puede volver a tirar")
                self.cambiar_jugador()
                return            
            elif numero==6 and len(self.ogl.historicodado)<3:
                self.lstLog_newLog("No es 5, pero puede volver a tirar")
                self.ogl.pendiente=2
                self.actionDado.setEnabled(True)
                self.cmdTirarDado.setEnabled(True)
                return

                
        

                    
    def cambiar_jugador(self):
        def limpia_panel(id):
            pix=pixdado(None)
            if id==0:
                self.panel1.lbl1.setPixmap(pix)
                self.panel1.lbl2.setPixmap(pix)
                self.panel1.lbl3.setPixmap(pix)
                self.panel1.show()
            elif id==1:
                self.panel2.lbl1.setPixmap(pix)
                self.panel2.lbl2.setPixmap(pix)
                self.panel2.lbl3.setPixmap(pix)
                self.panel2.show()
            elif id==2:
                self.panel3.lbl1.setPixmap(pix)
                self.panel3.lbl2.setPixmap(pix)
                self.panel3.lbl3.setPixmap(pix)
                self.panel3.show()
            elif id==3:
                self.panel4.lbl1.setPixmap(pix)
                self.panel4.lbl2.setPixmap(pix)
                self.panel4.lbl3.setPixmap(pix)
                self.panel4.show()
        self.ogl.jugadoractual=self.ogl.jugadoractual+1
        self.ogl.historicodado=[]
        self.ogl.pendiente=2
        if self.ogl.jugadoractual>=4:
            self.ogl.jugadoractual=0
#        self.lstLog_newLog("cambiando a jugador "  + str(self.ogl.jugadoractual))
        self.actionDado.setEnabled(True)       
        self.cmdTirarDado.setEnabled(True)
        self.enable_panel(self.ogl.jugadoractual,  True)
        limpia_panel(self.ogl.jugadoractual)

                    
    @QtCore.pyqtSlot()     
    def on_actionRecuperarPartida_activated(self):
        filename=QFileDialog.getOpenFileName(self, "", "", "glParchis game (*.glparchis)")
        self.ogl=wdgGame(filename)
#
#        names = []
#        values = []
#        f=open(filename)
#        dom = parse(f)
#        self.ogl.jugadoractual=int(dom.getElementsByTagName("jugadores")[0].getAttribute("actual"))
#        print self.ogl.jugadoractual
#        fichas=dom.getElementsByTagName("ficha")
#        for i in range(len(fichas)):
#            id=int(fichas[i].getAttribute("id"))
#            ruta=int(fichas[i].getAttribute("posicion_ruta"))
#            self.ogl.mover(id, ruta)


                    
    @QtCore.pyqtSlot()     
    def on_actionPartidaNueva_activated(self):
        def save_last_glparchis():
            try:
                os.remove(libglparchis.lastfile)
            except:
                pass
            config = ConfigParser.ConfigParser()
            for color in ['yellow', 'blue', 'red', 'green']:
                config.add_section(color)
                config.set(color,  'ia', int(self.jugadores[color].ia))
                config.set(color,  'name', self.jugadores[color].name)
                config.set(color,  'plays', int(self.jugadores[color].plays))
                config.set(color,  'rutaficha1', 1)
                config.set(color,  'rutaficha2', 2)
                config.set(color,  'rutaficha3', 3)
                config.set(color,  'rutaficha4', 0)
            config.add_section("game")
            config.set("game", 'playerstarts', initgame.playerstarts)
            with open(libglparchis.lastfile, 'w') as configfile:
                config.write(configfile)            
                
        initgame=frmInitGame()
        initgame.exec_()
        self.jugadores={}
        
        yellow=Jugador('yellow')
        yellow.name=initgame.txtYellow.text()
        yellow.ia=libglparchis.c2b(initgame.chkYellow.checkState())
        yellow.plays=libglparchis.c2b(initgame.chkYellowPlays.checkState())
        
        blue=Jugador('blue')
        blue.name=initgame.txtBlue.text()
        blue.ia=libglparchis.c2b(initgame.chkBlue.checkState())
        blue.plays=libglparchis.c2b(initgame.chkBluePlays.checkState())
        
        red=Jugador('red')
        red.name=initgame.txtRed.text()
        red.ia=libglparchis.c2b(initgame.chkRed.checkState())
        red.plays=libglparchis.c2b(initgame.chkRedPlays.checkState())
        
        green=Jugador('green')
        green.name=initgame.txtGreen.text()
        green.ia=libglparchis.c2b(initgame.chkGreen.checkState())
        green.plays=libglparchis.c2b(initgame.chkGreenPlays.checkState())
        
        self.jugadores['blue']=blue
        self.jugadores['yellow']=yellow
        self.jugadores['red']=red
        self.jugadores['green']=green
        
        self.panel1.grp.setTitle(self.jugadores['yellow'].name)
        self.panel2.grp.setTitle(self.jugadores['blue'].name)
        self.panel3.grp.setTitle(self.jugadores['red'].name)
        self.panel4.grp.setTitle(self.jugadores['green'].name)
        #Graba fichero .glparchis/last.glparchis
        save_last_glparchis()
        #Carga fichero .glparchis/last.glparchis
        self.ogl=wdgGame()
        self.ogl.load_file(libglparchis.lastfile)
    @QtCore.pyqtSlot()     
    def on_actionGuardarPartida_activated(self):
        filename=QFileDialog.getOpenFileName(self, "", "", "glParchis game (*.glparchis)")
        f=open(filename,"w")
        f.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
        f.write("<glParchis version=\"1.0\">\n")
        f.write("<partida>\n")
        f.write("  <jugadores numero=\""+str(4)+"\" actual=\""+str(self.ogl.jugadoractual)+"\">\n" )
        f.write('    <jugador id="0" nombre="amarillo" tipo="'+str(0)+'">\n') #Deberá ser cambiado cuando haya IA
        f.write("      <fichas>\n")
        f.write('        <ficha id="0" posicion_ruta="'+str(self.ogl.fichas[0].ruta)+'" />\n')
        f.write('        <ficha id="1" posicion_ruta="'+str(self.ogl.fichas[1].ruta)+'" />\n')
        f.write('        <ficha id="2" posicion_ruta="'+str(self.ogl.fichas[2].ruta)+'" />\n')
        f.write('        <ficha id="3" posicion_ruta="'+str(self.ogl.fichas[3].ruta)+'" />\n')
        f.write("      </fichas>\n")
        f.write("    </jugador>\n")
        f.write('    <jugador id="1" nombre="azul" tipo="'+str(0)+'">\n')
        f.write("      <fichas>\n")
        f.write('        <ficha id="4" posicion_ruta="'+str(self.ogl.fichas[4].ruta)+'" />\n')
        f.write('        <ficha id="5" posicion_ruta="'+str(self.ogl.fichas[5].ruta)+'" />\n')
        f.write('        <ficha id="6" posicion_ruta="'+str(self.ogl.fichas[6].ruta)+'" />\n')
        f.write('        <ficha id="7" posicion_ruta="'+str(self.ogl.fichas[7].ruta)+'" />\n')
        f.write("      </fichas>\n")
        f.write("    </jugador>\n")
        f.write('    <jugador id="2" nombre="rojo" tipo="'+str(0)+'">\n')
        f.write("      <fichas>\n")
        f.write('        <ficha id="8" posicion_ruta="'+str(self.ogl.fichas[8].ruta)+'" />\n')
        f.write('        <ficha id="9" posicion_ruta="'+str(self.ogl.fichas[9].ruta)+'" />\n')
        f.write('        <ficha id="10" posicion_ruta="'+str(self.ogl.fichas[10].ruta)+'" />\n')
        f.write('        <ficha id="11" posicion_ruta="'+str(self.ogl.fichas[11].ruta)+'" />\n')
        f.write("      </fichas>\n")
        f.write("    </jugador>\n")
        f.write('    <jugador id="3" nombre="verde" tipo="'+str(0)+'">\n')
        f.write("      <fichas>\n")
        f.write('        <ficha id="12" posicion_ruta="'+str(self.ogl.fichas[12].ruta)+'" />\n')
        f.write('        <ficha id="13" posicion_ruta="'+str(self.ogl.fichas[13].ruta)+'" />\n')
        f.write('        <ficha id="14" posicion_ruta="'+str(self.ogl.fichas[14].ruta)+'" />\n')
        f.write('        <ficha id="15" posicion_ruta="'+str(self.ogl.fichas[15].ruta)+'" />\n')
        f.write("      </fichas>\n")
        f.write("    </jugador>\n")
        f.write("  </jugadores>\n")
        f.write("  <dado ultima_tirada=\"5\" num_debugs=\"0\">\n");
        f.write("     <!-- <debug tirada=\"0\" /> -->\n");
        f.write("  </dado>\n")
        f.write("</partida>\n")
        f.write("</glParchis>\n")
        f.close()

    def volver_a_tirar(self):
        self.actionDado.setEnabled(True)
