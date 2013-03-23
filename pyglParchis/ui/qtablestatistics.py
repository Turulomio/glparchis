## -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from libglparchis import *
import datetime

class QTableStatistics(QTableWidget):
    def __init__(self, parent=None):
        QTableWidget.__init__(self, parent)    


    def assign_mem(self, mem):
        self.mem=mem
        
        
        #UI headers
        self.verticalHeader().setResizeMode(QHeaderView.ResizeToContents)
        self.horizontalHeader().setResizeMode(QHeaderView.ResizeToContents)
        self.setColumnCount(self.mem.maxplayers+1)        
        for i, j in enumerate(self.mem.jugadores.arr):

            
            item = QTableWidgetItem()
            item.setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter|Qt.AlignCenter)
            item.setIcon(j.color.qicon())
            self.setHorizontalHeaderItem(i, item)
        item = QTableWidgetItem(self.trUtf8("Total"))
        item.setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter|Qt.AlignCenter)
#        icon11 = QIcon()
#        icon11.addPixmap(QPixmap(":/glparchis/star.png"), QIcon.Normal, QIcon.Off)
#        item.setIcon(icon11)
        self.setHorizontalHeaderItem(self.mem.maxplayers, item)
        
        #Crea items
        for i in range(self.mem.maxplayers+1+1):
            for j in range(17):
                item=QTableWidgetItem()
                item.setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter|Qt.AlignCenter)
                self.setItem( j,i, item )
                
        #Rallando la tabla
        for i, j in ((9, self.mem.maxplayers), (10, self.mem.maxplayers), (14, self.mem.maxplayers), (16, self.mem.maxplayers)):
            item = QTableWidgetItem()
            item.setTextAlignment(Qt.AlignRight|Qt.AlignVCenter)
            brush = QBrush(QColor(0, 0, 0))
            brush.setStyle(Qt.BDiagPattern)
            item.setBackground(brush)
            self.setItem(i, j, item)
            
#        for i in range(1, self.mem.maxplayers):
#            item = QTableWidgetItem()
#            item.setTextAlignment(Qt.AlignRight|Qt.AlignVCenter)
#            brush = QBrush(QColor(0, 0, 0))
#            brush.setStyle(Qt.BDiagPattern)
#            item.setBackground(brush)
#            self.setItem(16, i, item)

        #negrita
#        item = QTableWidgetItem()
#        item.setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter|Qt.AlignCenter)
#        font = QFont()
#        font.setBold(True)
#        font.setWeight(75)
#        item.setFont(font)
#        self.setItem(16, 0, item)
                

    
    def reload(self):
        #Define el widget cron para que aparezca centrado el icon dentro de qtableitem
        crown=QWidget()
        lay=QHBoxLayout(crown)
        lay.addSpacing(0)
        pix = QLabel()
        pix.setMaximumSize(QSize(24, 24))
        pix.setScaledContents(True)
        pix.setPixmap(QPixmap(":/glparchis/corona.png"))
        pix.setAlignment(Qt.AlignCenter)
        lay.addWidget(pix)
        lay.addSpacing(0)
        crown.setLayout(lay)
        
        tj=TiradaJuego(self.mem)
        ganando=self.mem.jugadores.vaGanando()
        for j in self.mem.jugadores.arr:
            column=self.mem.colores.index(j.color)
            self.item(0, column).setText(str(j.tiradahistorica.numThrows()))
            for i in range(2, 8):
                self.item(i, column).setText(str(j.tiradahistorica.numTimesDiceGetNumber(i-1)))
            self.item(9, column).setText(str(j.comidaspormi))
            self.item(10, column).setText(str(j.comidasporotro))
            self.item(12, column).setText(str(j.tiradahistorica.numThreeSixes()))
            
            
            if j==ganando:
                self.setCellWidget(13, column, crown)    
            else:
                w=QWidget()
                self.setCellWidget(13, column, w)
            
            item=QTableWidgetItem(str(j.casillasMovidas()))
            item.setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter)
            self.setItem(14, column, item)    
    
            self.item(16, column).setText(str(self.mem.jugadores.score(j)))
            
        self.item(0, self.mem.maxplayers).setText(str(tj.numThrows()))
        for i in range(2, 8):
            self.item(i, self.mem.maxplayers).setText(str(tj.numTimesDiceGetNumber(i-1)))
        self.item(12, self.mem.maxplayers).setText(str(tj.numThreeSixes()))
        

