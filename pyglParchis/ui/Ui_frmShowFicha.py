# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/frmShowFicha.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_frmShowFicha(object):
    def setupUi(self, frmShowFicha):
        frmShowFicha.setObjectName("frmShowFicha")
        frmShowFicha.resize(507, 330)
        frmShowFicha.setStyleSheet("background-color: rgb(253, 255, 190);")
        self.horizontalLayout = QtWidgets.QHBoxLayout(frmShowFicha)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(frmShowFicha)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lblName = QtWidgets.QLabel(self.tab)
        self.lblName.setAlignment(QtCore.Qt.AlignCenter)
        self.lblName.setObjectName("lblName")
        self.verticalLayout.addWidget(self.lblName)
        self.lblFicha = QtWidgets.QLabel(self.tab)
        self.lblFicha.setText("")
        self.lblFicha.setPixmap(QtGui.QPixmap(":/glparchis/fichaamarilla.png"))
        self.lblFicha.setAlignment(QtCore.Qt.AlignCenter)
        self.lblFicha.setObjectName("lblFicha")
        self.verticalLayout.addWidget(self.lblFicha)
        self.lblJugador = QtWidgets.QLabel(self.tab)
        self.lblJugador.setAlignment(QtCore.Qt.AlignCenter)
        self.lblJugador.setObjectName("lblJugador")
        self.verticalLayout.addWidget(self.lblJugador)
        self.lblRuta = QtWidgets.QLabel(self.tab)
        self.lblRuta.setAlignment(QtCore.Qt.AlignCenter)
        self.lblRuta.setObjectName("lblRuta")
        self.verticalLayout.addWidget(self.lblRuta)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tblAmenazas = QtWidgets.QTableWidget(self.tab_2)
        self.tblAmenazas.setStyleSheet("background-color: rgb(253, 255, 190);")
        self.tblAmenazas.setObjectName("tblAmenazas")
        self.tblAmenazas.setColumnCount(3)
        self.tblAmenazas.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tblAmenazas.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblAmenazas.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblAmenazas.setHorizontalHeaderItem(2, item)
        self.horizontalLayout_3.addWidget(self.tblAmenazas)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.tab_3)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(self.tab_3)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.cmbDestino = QtWidgets.QComboBox(self.tab_3)
        self.cmbDestino.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.cmbDestino.setObjectName("cmbDestino")
        self.cmbDestino.addItem("")
        self.cmbDestino.addItem("")
        self.cmbDestino.addItem("")
        self.cmbDestino.addItem("")
        self.cmbDestino.addItem("")
        self.cmbDestino.addItem("")
        self.cmbDestino.addItem("")
        self.cmbDestino.addItem("")
        self.cmbDestino.addItem("")
        self.cmbDestino.addItem("")
        self.horizontalLayout_4.addWidget(self.cmbDestino)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.group = QtWidgets.QGroupBox(self.tab_3)
        self.group.setObjectName("group")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.group)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.tblAmenazasDestino = QtWidgets.QTableWidget(self.group)
        self.tblAmenazasDestino.setStyleSheet("background-color: rgb(253, 255, 190);")
        self.tblAmenazasDestino.setObjectName("tblAmenazasDestino")
        self.tblAmenazasDestino.setColumnCount(3)
        self.tblAmenazasDestino.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tblAmenazasDestino.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblAmenazasDestino.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblAmenazasDestino.setHorizontalHeaderItem(2, item)
        self.horizontalLayout_5.addWidget(self.tblAmenazasDestino)
        self.verticalLayout_3.addWidget(self.group)
        self.horizontalLayout_6.addLayout(self.verticalLayout_3)
        self.tabWidget.addTab(self.tab_3, "")
        self.horizontalLayout.addWidget(self.tabWidget)

        self.retranslateUi(frmShowFicha)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(frmShowFicha)

    def retranslateUi(self, frmShowFicha):
        _translate = QtCore.QCoreApplication.translate
        self.lblName.setText(_translate("frmShowFicha", "TextLabel"))
        self.lblJugador.setText(_translate("frmShowFicha", "TextLabel"))
        self.lblRuta.setText(_translate("frmShowFicha", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("frmShowFicha", "Informacion"))
        item = self.tblAmenazas.horizontalHeaderItem(0)
        item.setText(_translate("frmShowFicha", "Ficha"))
        item = self.tblAmenazas.horizontalHeaderItem(1)
        item.setText(_translate("frmShowFicha", "Casilla"))
        item = self.tblAmenazas.horizontalHeaderItem(2)
        item.setText(_translate("frmShowFicha", "Amenaza"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("frmShowFicha", "Amenazas"))
        self.label.setText(_translate("frmShowFicha", "Numero de casillas a avanzar"))
        self.cmbDestino.setItemText(0, _translate("frmShowFicha", "Selecciona un numero"))
        self.cmbDestino.setItemText(1, _translate("frmShowFicha", "1"))
        self.cmbDestino.setItemText(2, _translate("frmShowFicha", "2"))
        self.cmbDestino.setItemText(3, _translate("frmShowFicha", "3"))
        self.cmbDestino.setItemText(4, _translate("frmShowFicha", "4"))
        self.cmbDestino.setItemText(5, _translate("frmShowFicha", "5"))
        self.cmbDestino.setItemText(6, _translate("frmShowFicha", "6"))
        self.cmbDestino.setItemText(7, _translate("frmShowFicha", "7"))
        self.cmbDestino.setItemText(8, _translate("frmShowFicha", "10"))
        self.cmbDestino.setItemText(9, _translate("frmShowFicha", "20"))
        self.group.setTitle(_translate("frmShowFicha", "Amenazas en la casilla X"))
        item = self.tblAmenazasDestino.horizontalHeaderItem(0)
        item.setText(_translate("frmShowFicha", "Ficha"))
        item = self.tblAmenazasDestino.horizontalHeaderItem(1)
        item.setText(_translate("frmShowFicha", "Casilla"))
        item = self.tblAmenazasDestino.horizontalHeaderItem(2)
        item.setText(_translate("frmShowFicha", "Amenaza"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("frmShowFicha", "Amenazas en destino"))

import glparchis_rc
