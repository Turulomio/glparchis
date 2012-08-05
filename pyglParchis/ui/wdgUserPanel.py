## -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import libglparchis, datetime

from Ui_wdgUserPanel import *

class wdgUserPanel(QWidget, Ui_wdgUserPanel):
    def __init__(self, parent = None, name = None):
        QWidget.__init__(self, parent)
        self.inittime=datetime.datetime.now()
        if name:
            self.setObjectName(name)
        self.setupUi(self)
        self.log=[]
        self.history=[]
        self.jugador=None
        
    def setJugador(self, jugador):
        self.jugador=jugador
        self.lblAvatar.setPixmap(jugador.qpixmap())      
        
        
#    @QtCore.pyqtSlot(bool)      
    def setActivated(self, bool):
        self.grp.setEnabled(bool)
        if bool==True:
            self.log=[]

    def newLog(self, log):
        log=str(datetime.datetime.now()-self.inittime)[2:-7]+ " " + log
        self.history.append( log)
        self.log.append(log)
        self.on_chk_stateChanged(self.chk.checkState())

    def on_chk_stateChanged(self, state):
        self.lst.clear()
        if libglparchis.c2b(state)==True:
            self.lst.addItems(self.history)  
            self.lst.setCurrentRow(len(self.history)-1)
        else:
            self.lst.addItems(self.log)          
            self.lst.setCurrentRow(len(self.log)-1)
#            QModelIndex modelIndex = list->rootIndex(); // u have to find the model index of the first item here
#list->setCurrentIndex(modelIndex);
#        self.lst.selectionModel().select(len(self.log)-1, QItemSelectionModel.Select)          
        self.lst.show()            
