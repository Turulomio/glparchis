# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'glparchis/ui/frmSettings.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_frmSettings(object):
    def setupUi(self, frmSettings):
        frmSettings.setObjectName("frmSettings")
        frmSettings.resize(536, 331)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/glparchis/configure.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        frmSettings.setWindowIcon(icon)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(frmSettings)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lblTitulo = QtWidgets.QLabel(frmSettings)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lblTitulo.setFont(font)
        self.lblTitulo.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTitulo.setObjectName("lblTitulo")
        self.verticalLayout.addWidget(self.lblTitulo)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.lblPixmap = QtWidgets.QLabel(frmSettings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblPixmap.sizePolicy().hasHeightForWidth())
        self.lblPixmap.setSizePolicy(sizePolicy)
        self.lblPixmap.setMinimumSize(QtCore.QSize(48, 48))
        self.lblPixmap.setMaximumSize(QtCore.QSize(48, 48))
        self.lblPixmap.setPixmap(QtGui.QPixmap(":/glparchis/configure.png"))
        self.lblPixmap.setScaledContents(True)
        self.lblPixmap.setAlignment(QtCore.Qt.AlignCenter)
        self.lblPixmap.setObjectName("lblPixmap")
        self.horizontalLayout_2.addWidget(self.lblPixmap)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(frmSettings)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.cmbLanguage = QtWidgets.QComboBox(frmSettings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmbLanguage.sizePolicy().hasHeightForWidth())
        self.cmbLanguage.setSizePolicy(sizePolicy)
        self.cmbLanguage.setObjectName("cmbLanguage")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.cmbLanguage)
        self.nMeroDeAutoguardadosLabel = QtWidgets.QLabel(frmSettings)
        self.nMeroDeAutoguardadosLabel.setObjectName("nMeroDeAutoguardadosLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.nMeroDeAutoguardadosLabel)
        self.spinAutosaves = QtWidgets.QSpinBox(frmSettings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinAutosaves.sizePolicy().hasHeightForWidth())
        self.spinAutosaves.setSizePolicy(sizePolicy)
        self.spinAutosaves.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spinAutosaves.setObjectName("spinAutosaves")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.spinAutosaves)
        self.cmbDifficultyLevel = QtWidgets.QComboBox(frmSettings)
        self.cmbDifficultyLevel.setObjectName("cmbDifficultyLevel")
        self.cmbDifficultyLevel.addItem("")
        self.cmbDifficultyLevel.addItem("")
        self.cmbDifficultyLevel.addItem("")
        self.cmbDifficultyLevel.addItem("")
        self.cmbDifficultyLevel.addItem("")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.cmbDifficultyLevel)
        self.label = QtWidgets.QLabel(frmSettings)
        self.label.setObjectName("label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lblSliderDelay = QtWidgets.QLabel(frmSettings)
        self.lblSliderDelay.setObjectName("lblSliderDelay")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lblSliderDelay)
        self.spinDelay = QtWidgets.QSpinBox(frmSettings)
        self.spinDelay.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spinDelay.setMinimum(0)
        self.spinDelay.setMaximum(2000)
        self.spinDelay.setSingleStep(100)
        self.spinDelay.setProperty("value", 300)
        self.spinDelay.setDisplayIntegerBase(10)
        self.spinDelay.setObjectName("spinDelay")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.spinDelay)
        self.horizontalLayout.addLayout(self.formLayout)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.chkStatistics = QtWidgets.QCheckBox(frmSettings)
        self.chkStatistics.setChecked(True)
        self.chkStatistics.setObjectName("chkStatistics")
        self.horizontalLayout_3.addWidget(self.chkStatistics)
        self.cmdGlobalStatistics = QtWidgets.QToolButton(frmSettings)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/glparchis/statistics.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cmdGlobalStatistics.setIcon(icon1)
        self.cmdGlobalStatistics.setObjectName("cmdGlobalStatistics")
        self.horizontalLayout_3.addWidget(self.cmdGlobalStatistics)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.buttonBox = QtWidgets.QDialogButtonBox(frmSettings)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)

        self.retranslateUi(frmSettings)
        self.buttonBox.accepted.connect(frmSettings.accept)
        self.buttonBox.rejected.connect(frmSettings.reject)
        QtCore.QMetaObject.connectSlotsByName(frmSettings)

    def retranslateUi(self, frmSettings):
        _translate = QtCore.QCoreApplication.translate
        frmSettings.setWindowTitle(_translate("frmSettings", "Configuracion de glParchis"))
        self.lblTitulo.setText(_translate("frmSettings", "Configuracion de glParchis"))
        self.label_2.setText(_translate("frmSettings", "Selecciona un idioma"))
        self.nMeroDeAutoguardadosLabel.setText(_translate("frmSettings", "Numero de autoguardados"))
        self.spinAutosaves.setToolTip(_translate("frmSettings", "Si quiere autoguardado seleccione un numero mayor que 0"))
        self.cmbDifficultyLevel.setItemText(0, _translate("frmSettings", "Facil"))
        self.cmbDifficultyLevel.setItemText(1, _translate("frmSettings", "Muy facil"))
        self.cmbDifficultyLevel.setItemText(2, _translate("frmSettings", "Normal"))
        self.cmbDifficultyLevel.setItemText(3, _translate("frmSettings", "Dificil"))
        self.cmbDifficultyLevel.setItemText(4, _translate("frmSettings", "Muy dificil"))
        self.label.setText(_translate("frmSettings", "Nivel de dificultad"))
        self.lblSliderDelay.setText(_translate("frmSettings", "Retardo entre movimientos"))
        self.spinDelay.setSuffix(_translate("frmSettings", " ms"))
        self.chkStatistics.setText(_translate("frmSettings", "Si esta marcado, tus partidas formaran parte de las estadisticas mundiales"))
        self.cmdGlobalStatistics.setToolTip(_translate("frmSettings", "Ver estadisticas"))

import glparchis.images.glparchis_rc
