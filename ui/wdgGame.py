# -*- coding: utf-8 -*-
import ConfigParser,  base64
from PyQt4.QtCore import *
from PyQt4.QtOpenGL import *
from PyQt4.QtGui import *
from wdgUserPanel import *
from wdgGame import *
from qtablestatistics import *
from libglparchis import *
from Ui_wdgGame import *

class wdgGame(QWidget, Ui_wdgGame):
    """Clase principal del Juego, aquí está toda la ciencia, cuando se deba pasar al UI se crearán emits que captura qT para el UI"""
    def __init__(self,   parent=None,  filename=None):        
        QWidget.__init__(self, parent)
        self.setupUi(self)
        self.show()
        self.panels=[]
        
        
        #Timer statistics
        self.timer = QTimer()
        QObject.connect(self.timer, SIGNAL("timeout()"), self.timer_reload)     
        self.timer.start(500)
        
    
    def __del__(self):
        print ("Destructor wdgGame")
        self.stopthegame=True
        self.stopReloads()
        for p in self.panels:
            p.stopTimerLog()
            self.panelScrollLayout.removeWidget(p)
        self.hide()
        
        
    
    def stopReloads(self):
        self.timer.stop()
        
    def timer_reload(self):
        self.table.reload()
        self.lblTime.setText(self.trUtf8("Tiempo de partida: {0}".format(str(datetime.datetime.now()-self.inicio).split(".")[0])))
        
        

    def assign_mem(self, mem):
        self.inicio=datetime.datetime.now()#tiempo de inicio
        self.mem=mem
        self.stopthegame=False
        self.table.assign_mem(self.mem)
        self.ogl.assign_mem(self.mem)
        self.ogl.setFocus()
        self.hs4=HighScore(self.mem, 4)
        self.hs6=HighScore(self.mem, 6)
        self.hs8=HighScore(self.mem, 8)
        self.highscoresUpdate()
        
        for j in self.mem.jugadores.arr:
            if j.plays:
                p=wdgUserPanel(self)
                self.panelScrollLayout.addWidget(p)
                p.setJugador(j)
                self.panels.append(p)
        
        self.panel().setActivated(True)
        self.cmdTirarDado.setStyleSheet('QPushButton {color: '+self.mem.jugadores.actual.color.name+'; font: bold 30px; background-color: rgb(170, 170, 170);}')
        self.mem.jugadores.actual.log(self.tr("Empieza la partida"))


        QtCore.QObject.connect(self.ogl, QtCore.SIGNAL('fichaClicked()'), self.after_ficha_click)  
        if self.mem.cfgfile.splitterstate==None:
            currentSizes = self.splitter.sizes()
            currentSizes[0]=self.width()-self.ogl.height()-100
            currentSizes[1]=self.width()-currentSizes[0]
            self.splitter.setSizes(currentSizes)
        else:
            self.splitter.restoreState(self.mem.cfgfile.splitterstate)
        
        #Coloca los tabs del widget
        self.tab.setCurrentIndex(0)
        if self.mem.maxplayers==4:
            self.tabHS.setCurrentIndex(0)
        elif self.mem.maxplayers==6:
            self.tabHS.setCurrentIndex(1)
        elif self.mem.maxplayers==8:
            self.tabHS.setCurrentIndex(2)
        
            
        self.connect(self.ogl, SIGNAL("doubleClicked()"), self.on_ogl_doubleClicked)
        self.mem.inittime=datetime.datetime.now()
        self.on_JugadorDebeTirar()

    def on_ogl_doubleClicked(self):
        if self.cmdTirarDado.isEnabled()==False:
            return
        self.on_cmdTirarDado_clicked()

    def panel(self, jugador=None):
        """Si se pasa sin parametro da el panel del jugador actual"""
        if jugador==None:
            jugador=self.mem.jugadores.actual
        for p in self.panels:
            if p.jugador==jugador:
                return p

    def afterWinning(self):
        self.mem.jugadores.actual.log(self.trUtf8("Has ganado la partida"))
        self.mem.jugadores.winner=self.mem.jugadores.actual
        self.mem.play("win")
        self.stopReloads()
        self.stopthegame=True
        for p in self.panels:
            p.stopTimerLog()
        if self.mem.jugadores.winner.ia==False:#Solo se genera hs cuando es un humano
            if self.mem.maxplayers==4:
                self.hs4.insert()
                self.hs4.save()
            elif self.mem.maxplayers==6:
                self.hs6.insert()
                self.hs6.save()
            elif self.mem.maxplayers==8:
                self.hs8.insert()
                self.hs8.save()           
            self.highscoresUpdate()
        
        m=QMessageBox()
        m.setIcon(QMessageBox.Information)
        m.setText(self.trUtf8("%1 ha ganado").arg(self.mem.jugadores.actual.name))
        m.exec_() 
        self.tab.setCurrentIndex(1)


    def on_JugadorDebeTirar(self):
        """Se ejecuta cuando el jugador debe tirar:
                - Inicio turno
                - Otras situaciones"""
        if self.stopthegame==True:
            return
        if self.mem.jugadores.alguienHaGanado()==True:
            self.afterWinning()
            return  
            
        self.cmdTirarDado.setText(self.trUtf8("Tira el dado"))
        if self.mem.jugadores.actual.ia==False:#Cuando es IA no debe permitir tirar dado
            self.cmdTirarDado.setEnabled(True)
#        self.cmdTirarDado.setIcon(self.mem.dado.qicon(None))
        if self.mem.jugadores.actual.ia==True:
            self.mem.jugadores.actual.log(self.trUtf8(u"IA Tira el dado"))
            delay(400)
            self.on_cmdTirarDado_clicked()
            delay(800)
        else:
            self.mem.jugadores.actual.log(self.trUtf8(u"Tire el dado"))

       
    def on_JugadorDebeMover(self):
        """Función que se ejecuta cuando un jugador debe mover
        Aquí se evalua si puede mover devolviendo True en caso positivo y """
        
        if self.mem.jugadores.alguienHaGanado()==True:
            self.afterWinning()
            return
        
        self.cmdTirarDado.setEnabled(False)
        if self.mem.jugadores.actual.ia==True:
            self.mem.jugadores.actual.log(self.trUtf8("IA mueve una ficha"))     
            iaficha=self.mem.jugadores.actual.IASelectFicha(self.mem)
            delay(400)
            if iaficha==None:
                self.cambiarJugador()
            else:
                self.mem.selFicha=iaficha
                self.after_ficha_click()
        else:
            self.mem.jugadores.actual.log(self.trUtf8("Mueva una ficha"))

        
    def on_splitter_splitterMoved(self, position, index):
        self.mem.cfgfile.splitterstate=self.splitter.saveState()
#        print self.mem.cfgfile.splitterstate,  base64.b64encode(self.mem.cfgfile.splitterstate)
        self.mem.cfgfile.save()
        self.update()

    @QtCore.pyqtSlot()      
    def on_cmdTirarDado_clicked(self):  
        self.cmdTirarDado.setEnabled(False)
        self.cmdTirarDado.setText("")
        self.mem.play("dice")
        self.mem.jugadores.actual.tirarDado()
        self.mem.dado.showing=True
        self.ogl.updateGL()
#        self.cmdTirarDado.setIcon(self.mem.dado.qicon(self.mem.jugadores.actual.tiradaturno.ultimoValor()))
        self.panel().setLabelDado()
        
        if self.mem.jugadores.actual.tiradaturno.tresSeises()==True:
            if self.mem.jugadores.actual.LastFichaMovida!=None:
                casilla=self.mem.jugadores.actual.LastFichaMovida.casilla()
                if casilla.rampallegada==True:
                    self.mem.jugadores.actual.log(self.trUtf8("Han salido tres seises, no se va a casa por haber llegado a rampa de llegada"))
                else:
                    if self.mem.jugadores.actual.LastFichaMovida.estaAutorizadaAMover(self.mem)[0]==True:
                        self.mem.jugadores.actual.log(self.trUtf8("Han salido tres seises, la ultima ficha movida se va a casa"))
                        self.mem.play("comer")
                        self.mem.jugadores.actual.LastFichaMovida.mover(0)
                    else:
                        self.mem.jugadores.actual.log(self.trUtf8(u"Han salido tres seises, pero como no puede mover no se va a casa"))
            else:               
                self.mem.jugadores.actual.log(self.trUtf8(u"Despues de tres seises, ya no puede volver a tirar"))
            self.cambiarJugador()
        else: # si no han salido 3 seises
            if self.mem.jugadores.actual.fichas.algunaEstaAutorizadaAmover(self.mem)==True:
                self.on_JugadorDebeMover()
            else:#ninguna puede mover.
                if self.mem.jugadores.actual.tiradaturno.ultimoEsSeis()==True:
                    self.on_JugadorDebeTirar()
                else:            
                    self.cambiarJugador()

    def after_ficha_click(self):
        if self.mem.selFicha==None:
            self.mem.jugadores.actual.log(self.trUtf8("Seleccione una ficha..."))
            return
            
        if self.cmdTirarDado.isEnabled():#Esta esperando dado no se puede pulsar ficha para mover.
            return
        
        (puede, movimiento)=self.mem.selFicha.estaAutorizadaAMover(self.mem, True)
            
        if puede==False:
            if self.mem.jugadores.actual.ia==False:
                self.mem.play("click")
            return

                
        if self.mem.selFicha.come(self.mem, self.mem.selFicha.posruta+movimiento) or self.mem.selFicha.mete(self.mem.selFicha.posruta+movimiento):    
            self.ogl.updateGL()
            if self.mem.jugadores.actual.movimientos_acumulados==10:
                self.mem.play("meter")
            else:
                self.mem.play("comer")            
            delay(600)
            if self.mem.jugadores.actual.fichas.algunaEstaAutorizadaAmover(self.mem)==True:
                self.on_JugadorDebeMover()
                return
        else:
            self.mem.selFicha.mover( self.mem.selFicha.posruta + movimiento)    
            self.ogl.updateGL()
       #Quita el movimiento acumulados
        if self.mem.jugadores.actual.movimientos_acumulados in (10, 20):
            self.mem.jugadores.actual.movimientos_acumulados=None

        if self.mem.jugadores.actual.tiradaturno.ultimoEsSeis()==True:
            self.on_JugadorDebeTirar()
        else:
            self.cambiarJugador()

    def cambiarJugador(self):          
        if self.mem.jugadores.alguienHaGanado()==True:
            self.afterWinning()
            return          
        self.mem.jugadores.actual.log (self.trUtf8("Fin de turno"))
        self.ogl.updateGL()        
        delay(400)
        self.mem.dado.showing=False
        self.ogl.updateGL()        

        self.panel().setActivated(False)
        self.panel().grp.update()
        
        self.mem.jugadores.cambiarJugador()
        
        
        
        #Realiza el autosave
        if self.mem.cfgfile.autosaves>0 and self.mem.jugadores.actual.ia==False:
            #Borra el n-esimo autosave
            autosaves=[]
            for infile in glob.glob( os.path.join(os.path.expanduser("~/.glparchis/"), 'autosave_*.glparchis') ):
                autosaves.append(infile)
            autosaves.sort()
            if len(autosaves)>=self.mem.cfgfile.autosaves:
                for f in autosaves[:len(autosaves)-self.mem.cfgfile.autosaves+1]:
                    os.unlink(f)
            #Graba el ultimo autosave
            n=datetime.datetime.now()
            dt="{0}{1:02d}{2:02d}_{3:02d}{4:02d}{5:02d}".format(n.year, n.month, n.day, n.hour, n.minute, n.second)
            self.mem.save("autosave_{0}_{1}_{2}.glparchis".format(dt, self.mem.maxplayers, self.mem.jugadores.actual.color.name ))
        
        if self.chkAvanza.isChecked()==True:
            self.panelScroll.ensureWidgetVisible(self.panel())
        self.panel().setActivated(True) #Activa y limpia panel
        self.panel().grp.update()

        self.cmdTirarDado.setStyleSheet('QPushButton {color: '+self.mem.jugadores.actual.color.name+'; font: bold 30px; background-color: rgb(170, 170, 170);}')
        self.on_JugadorDebeTirar()

    def highscoresUpdate(self):
        def updateTable(hs, table): 
            table.verticalHeader().setResizeMode(QHeaderView.ResizeToContents)
            table.horizontalHeader().setResizeMode(QHeaderView.ResizeToContents)
            table.setRowCount(len(hs.arr))        
            for i,  a in enumerate(hs.arr):
                table.setItem(i, 0, QTableWidgetItem(str(datetime.date.fromordinal(int(a[0])))))
                item = QTableWidgetItem(a[1])
                item.setIcon(colores.colorbyname(a[3]).qicon())                
                table.setItem(i, 1, QTableWidgetItem(item))
                item = QTableWidgetItem(str(datetime.timedelta(seconds=int(a[2]))))
                item.setTextAlignment(Qt.AlignRight)
                table.setItem(i, 2, item)
                item = QTableWidgetItem(a[4])
                item.setTextAlignment(Qt.AlignRight)
                table.setItem(i, 3, item)
        #############################
        colores=SetColores()
        colores.generar_colores(8)
        updateTable(self.hs4, self.tblHighScores4)
        updateTable(self.hs6, self.tblHighScores6)
        updateTable(self.hs8, self.tblHighScores8)
