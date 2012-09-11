# -*- coding: utf-8 -*-
import sys,    os
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from libglparchis import *

from Ui_frmMain import *
from wdgGame import *
from frmAbout import *
from frmInitGame import *
from frmSettings import *

            
class frmMain(QMainWindow, Ui_frmMain):#    
    def __init__(self, parent = 0,  flags = False):
        QMainWindow.__init__(self, None)
        self.setupUi(self)
        self.showMaximized()
        self.game=None
        self.on_actionPartidaNueva_activated()
        
######    @pyqtSignature("")
    @pyqtSlot()      
    def on_actionAcercaDe_activated(self):
        fr=frmAbout(self, "frmabout")
        print("nosequepasa")
        fr.open()
        
    @QtCore.pyqtSlot()      
    def on_actionSettings_activated(self):
        f=frmSettings(self)
        f.exec_()
        
    @QtCore.pyqtSlot()      
    def on_actionSalir_activated(self):
        sys.exit()
  
    def showWdgGame(self):
        if self.game!=None:
            self.layout.removeWidget(self.game)
        self.game=wdgGame()
        self.layout.addWidget(self.game)
        self.game.assign_mem(self.mem)
        self.actionGuardarPartida.setEnabled(True)
        

    @QtCore.pyqtSlot()     
    def on_actionRecuperarPartida_activated(self):
        #ÐEBE SERLOCAL
        filenam=os.path.basename(libglparchis.q2s(QFileDialog.getOpenFileName(self, "", "", "glParchis game (*.glparchis)")))
        if filenam!="":
            self.mem=Mem4()
            self.mem.load(filenam)
            self.showWdgGame()


    @QtCore.pyqtSlot()     
    def on_actionPartidaNueva_activated(self):
        self.mem=Mem4()
        initgame=frmInitGame(self.mem)
        initgame.exec_()
        self.showWdgGame()



    @QtCore.pyqtSlot()     
    def on_actionGuardarPartida_activated(self):
        filename=os.path.basename(libglparchis.q2s(QFileDialog.getOpenFileName(self, "", "", "glParchis game (*.glparchis)")))
        if filename!="":
            self.mem.save(filename)
