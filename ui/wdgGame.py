# -*- coding: utf-8 -*-
import ConfigParser
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

    def assign_mem(self, mem):
        def settings_splitter_load():
            config = ConfigParser.ConfigParser()
            config.read(libglparchis.cfgfile)
            try:
                position=config.get("frmMain", "splitter_state")
                self.splitter.restoreState(position)
            except:
                print ("No hay fichero de configuración")    
        self.mem=mem
        self.table.assign_mem(self.mem)
        self.ogl.assign_mem(self.mem)
        self.ogl.setFocus()
        
        self.panel1.setJugador(self.mem.jugadores.jugador("yellow"))
        self.panel2.setJugador(self.mem.jugadores.jugador("blue"))
        self.panel3.setJugador(self.mem.jugadores.jugador("red"))
        self.panel4.setJugador(self.mem.jugadores.jugador("green"))
        
        self.panel().setActivated(True)
        self.mem.jugadoractual.log(self.trUtf8("Empieza la partida"))


        QtCore.QObject.connect(self.ogl, QtCore.SIGNAL('fichaClicked()'), self.after_ficha_click)  
        settings_splitter_load()

#        self.cmdTirarDado.setGeometry(100, 100, 200, 64)
#        self.cmdTirarDado.setIconSize(QSize(80, 80 ))
#        self.cmdTirarDado.setParent(None)
#        self.cmdTirarDado.setWindowFlags(Qt.WindowStaysOnTopHint)
#        self.cmdTirarDado.setWindowTitle(self.trUtf8("Dado"))
#        self.cmdTirarDado.show()

        self.on_JugadorDebeTirar()

    def panel(self, jugador=None):
        """Si se pasa sin parametro da el panel del jugador actual"""
        if jugador==None:
            jugador=self.mem.jugadoractual
        if self.panel1.jugador==jugador:
            return self.panel1
        elif self.panel2.jugador==jugador:
            return self.panel2
        elif self.panel3.jugador==jugador:
            return self.panel3
        elif self.panel4.jugador==jugador:
            return self.panel4


    def on_JugadorDebeTirar(self):
        """Se ejecuta cuando el jugador debe tirar:
                - Inicio turno
                - Otras situaciones"""
        if self.mem.jugadoractual.ia==False:#Cuando es IA no debe permitir tirar dado
            self.cmdTirarDado.setEnabled(True)
        self.cmdTirarDado.setIcon(self.mem.dado.qicon(None))
#        self.cmdTirarDado.setText(self.trUtf8("Pulsa para tirar el dado"))
        if self.mem.jugadoractual.ia==True:
            self.mem.jugadoractual.log(self.trUtf8("IA Tira el dado"))
            delay(800)
            self.on_cmdTirarDado_clicked()
        else:
            self.mem.jugadoractual.log(self.trUtf8("Tire el dado"))

       
    def on_JugadorDebeMover(self):
        """Función que se ejecuta cuando un jugador debe mover
        Aquí se evalua si puede mover devolviendo True en caso positivo y """
        self.cmdTirarDado.setEnabled(False)
        if self.mem.jugadoractual.ia==True:
            self.mem.jugadoractual.log(self.trUtf8("IA mueve una ficha"))     
            iaficha=self.mem.jugadoractual.IASelectFicha(self.mem)
            delay(250)
            print (iaficha)
            if iaficha==None:
                self.cambiarJugador()
            else:
                self.mem.selFicha=iaficha
                self.after_ficha_click()
        else:
            self.mem.jugadoractual.log(self.trUtf8("Mueva una ficha"))

        
    def on_splitter_splitterMoved(self, position, index):
        config = ConfigParser.ConfigParser()
        config.read(libglparchis.cfgfile)
        if config.has_section("frmMain")==False:
            config.add_section("frmMain")
        config.set("frmMain",  'splitter_state', self.splitter.saveState())
        with open(libglparchis.cfgfile, 'w') as configfile:
            config.write(configfile)

    @QtCore.pyqtSlot()      
    def on_cmdTirarDado_clicked(self):  
        sound("dice")
        self.mem.jugadoractual.tirarDado()
        self.ogl.showDado()
#        self.emit(SIGNAL("dadoClicked()"))#No se pasa parámetro porque es self.mem.selFicha
        self.cmdTirarDado.setIcon(self.mem.dado.qicon(self.mem.jugadoractual.tiradaturno.ultimoValor()))
        self.cmdTirarDado.setEnabled(False)
        self.panel().setLabelDado()
        
        if self.mem.jugadoractual.tiradaturno.tresSeises()==True:
            if self.mem.jugadoractual.LastFichaMovida!=None:
                casilla=self.mem.jugadoractual.LastFichaMovida.casilla()
                if casilla.rampallegada==True:
                    self.mem.jugadoractual.log(self.trUtf8("Han salido tres seises, no se va a casa por haber llegado a rampa de llegada"))
                else:
                    if self.mem.jugadoractual.LastFichaMovida.puedeMover(self.mem)[0]==True:
                        self.mem.jugadoractual.log(self.trUtf8("Han salido tres seises, la ultima ficha movida se va a casa"))
                        self.mem.jugadoractual.LastFichaMovida.mover(0)
                    else:
                        self.mem.jugadoractual.log(self.trUtf8(u"Han salido tres seises, pero como no puede mover no se va a casa"))
            else:               
                self.mem.jugadoractual.log(self.trUtf8(u"Despues de tres seises, ya no puede volver a tirar"))
            self.cambiarJugador()
        else: # si no han salido 3 seises
            if self.mem.jugadoractual.fichas.algunaPuedeMover(self.mem)==True:
#                self.mem.jugadoractual.log(self.trUtf8("Mueva una ficha"))
                self.on_JugadorDebeMover()
            else:#ninguna puede mover.
                if self.mem.jugadoractual.tiradaturno.ultimoEsSeis()==True:
                    self.on_JugadorDebeTirar()
                else:            
                    self.cambiarJugador()

    def after_ficha_click(self):
        if self.cmdTirarDado.isEnabled():#Esta esperando dado no se puede pulsar ficha para mover.
            return
        puede=self.mem.selFicha.puedeMover(self.mem)
        if puede[0]==False:
            if self.mem.jugadoractual.ia==False:
                sound("click")
            self.mem.jugadoractual.log(self.trUtf8("No puede mover esta ficha, seleccione otra"))
            return
 
            #Come o mete
        
        if self.mem.selFicha.come(self.mem, self.mem.selFicha.posruta+puede[1]) or self.mem.selFicha.mete(self.mem.selFicha.posruta+puede[1]):    
            self.ogl.updateGL()
            sound("comer")
            if self.mem.jugadoractual.fichas.algunaPuedeMover(self.mem)==True:
                self.on_JugadorDebeMover()
                return
        else:
            self.mem.selFicha.mover( self.mem.selFicha.posruta + puede[1])    
            self.ogl.updateGL()
       #Quita el movimiento acumulados
        if self.mem.jugadoractual.movimientos_acumulados in (10, 20):
            self.mem.jugadoractual.movimientos_acumulados=None


 
#
#        if self.mem.selFicha.comeEnInicio():            
#            self.ogl.updateGL()
#            sound("comer")
#            if self.mem.jugadoractual.fichas.algunaPuedeMover(self.mem)==True:
#                self.on_JugadorDebeMover()
#                return
#        else:
#            self.mem.selFicha.mover( self.mem.selFicha.posruta + puede[1])    
#            self.ogl.updateGL()
#            #Quita el movimiento acumulados
#            if self.mem.jugadoractual.movimientos_acumulados in (10, 20):
#                self.mem.jugadoractual.movimientos_acumulados=None
#    
#            #Come o mete
#            if self.mem.selFicha.come(self.mem, self.mem.selFicha.posruta) or self.mem.selFicha.mete():    
#                self.ogl.updateGL()
#                sound("comer")
#                if self.mem.jugadoractual.fichas.algunaPuedeMover(self.mem)==True:
#                    self.on_JugadorDebeMover()
#                    return
        
        if self.mem.jugadoractual.tiradaturno.ultimoEsSeis()==True:
            self.on_JugadorDebeTirar()
        else:
            self.cambiarJugador()



    def cambiarJugador(self):          
        self.mem.jugadoractual.log ("{0} acaba el turno".format(self.mem.jugadoractual))
        self.ogl.updateGL()        
        delay(250)
        self.ogl.dado.hide()
        #Comprueba si ha ganado
        if self.mem.jugadoractual.HaGanado()==True:
            sound("win")
            m=QMessageBox()
            m.setIcon(QMessageBox.Information)
            m.setText(self.trUtf8("%1 ha ganado").arg(self.mem.jugadoractual.name))
            m.exec_() 
            self.tab.setCurrentIndex(1)
            return
        
        
        self.panel().setActivated(False)
#        if self.mem.jugadoractual.ia==True:
#            time.sleep(0.2)
        while True:
            if self.mem.jugadoractual.color.name=="yellow":
                self.mem.jugadoractual=self.mem.jugadores.jugador("blue")
            elif self.mem.jugadoractual.color.name=="blue" :
                self.mem.jugadoractual=self.mem.jugadores.jugador("red")
            elif self.mem.jugadoractual.color.name=="red" :
                self.mem.jugadoractual=self.mem.jugadores.jugador("green")
            elif self.mem.jugadoractual.color.name=="green" :
                self.mem.jugadoractual=self.mem.jugadores.jugador("yellow")
            if self.mem.jugadoractual.plays:#Comprueba si el actual plays y sale del bucle
                break

        self.mem.jugadoractual.tiradaturno=TiradaTurno()#Se crea otro objeto porque así el anterior queda vinculada< a TiradaHistorica.
        self.mem.jugadoractual.movimientos_acumulados=None
        self.mem.jugadoractual.LastFichaMovida=None
        
        #Activa y limpia
        self.panel().setActivated(True)
        self.panel().lbl1.setPixmap(self.mem.dado.qpixmap(None))
        self.panel().lbl2.setPixmap(self.mem.dado.qpixmap(None))
        self.panel().lbl3.setPixmap(self.mem.dado.qpixmap(None))
        self.panel().show()

        self.cmdTirarDado.setStyleSheet('QPushButton {color: '+self.mem.jugadoractual.color.name+'}')

        self.on_JugadorDebeTirar()


