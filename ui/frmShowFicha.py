## -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Ui_frmShowFicha import *   

class frmShowFicha(QDialog, Ui_frmShowFicha):
    def __init__(self,   parent = None, flags= None,  ficha=None, mem=None):
        QDialog.__init__(self, parent, flags)
        self.mem=mem
        self.ficha=ficha
        self.setupUi(self)
        self.lblFicha.setPixmap(self.ficha.jugador.color.qpixmap())       
        self.lblName.setText(self.trUtf8("Nombre: %1").arg(self.ficha.id))
        self.lblJugador.setText(self.trUtf8("Jugador: %1 (%2)").arg(str(self.ficha.jugador.name)).arg(self.ficha.jugador.color.name))
        self.lblRuta.setText(self.trUtf8("Posición en ruta: %1").arg(str(self.ficha.posruta)))
        self.tblAmenazas_reload()
        if self.mem.jugadores.actual.tiradaturno.ultimoValor()!=None:
            (puedemover, movimiento)=self.ficha.puedeMover(self.mem)
            if puedemover==True:
                self.cmbDestino.setCurrentIndex(self.cmbDestino.findText(str(movimiento)))
                self.on_cmbDestino_currentIndexChanged(str(movimiento))

    def tblAmenazas_reload(self):
        self.table_reload(self.tblAmenazas, self.ficha.amenazas(self.mem))

    @pyqtSlot(QString)      
    def on_cmbDestino_currentIndexChanged(self, stri):
        self.group.setTitle(self.trUtf8("Amenazas en la casilla {0}".format(self.ficha.casilla(self.ficha.posruta+int(stri)).id)))
        self.table_reload(self.tblAmenazasDestino, self.ficha.amenazasDestino(self.mem, int(stri)))
                
        
    def table_reload(self, table, setamenazas):
        table.verticalHeader().setResizeMode(QHeaderView.ResizeToContents)
        table.horizontalHeader().setResizeMode(QHeaderView.ResizeToContents)
        table.setRowCount(len(setamenazas.arr))        
        for i,  a in enumerate(setamenazas.arr):
            item = QTableWidgetItem()
            item.setIcon(a.atacante.color.qicon())                
            table.setItem(i, 0, QTableWidgetItem(item))
            item = QTableWidgetItem(str(a.atacante.casilla().id))
            item.setTextAlignment(Qt.AlignCenter)
            table.setItem(i, 1, item)
            item = QTableWidgetItem(a.name())
            table.setItem(i, 2, item)
