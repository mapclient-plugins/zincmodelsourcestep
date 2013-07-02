# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt/configuredialog.ui'
#
# Created: Wed Jul  3 01:19:35 2013
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ConfigureDialog(object):
    def setupUi(self, ConfigureDialog):
        ConfigureDialog.setObjectName("ConfigureDialog")
        ConfigureDialog.resize(593, 253)
        self.verticalLayout_2 = QtGui.QVBoxLayout(ConfigureDialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtGui.QGroupBox(ConfigureDialog)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.identifierLineEdit = QtGui.QLineEdit(self.groupBox)
        self.identifierLineEdit.setObjectName("identifierLineEdit")
        self.gridLayout.addWidget(self.identifierLineEdit, 0, 1, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.dataLineEdit = QtGui.QLineEdit(self.groupBox)
        self.dataLineEdit.setStyleSheet("selection-color: red;\n"
"color: green")
        self.dataLineEdit.setObjectName("dataLineEdit")
        self.horizontalLayout.addWidget(self.dataLineEdit)
        self.dataButton = QtGui.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.dataButton.setFont(font)
        self.dataButton.setObjectName("dataButton")
        self.horizontalLayout.addWidget(self.dataButton)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setMinimumSize(QtCore.QSize(71, 0))
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 1, 1, 1)
        self.previousLocationLabel = QtGui.QLabel(self.groupBox)
        self.previousLocationLabel.setMaximumSize(QtCore.QSize(0, 16777215))
        self.previousLocationLabel.setText("")
        self.previousLocationLabel.setObjectName("previousLocationLabel")
        self.gridLayout.addWidget(self.previousLocationLabel, 3, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.buttonBox = QtGui.QDialogButtonBox(ConfigureDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)
        self.label_3.setBuddy(self.dataLineEdit)
        self.label.setBuddy(self.identifierLineEdit)

        self.retranslateUi(ConfigureDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), ConfigureDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), ConfigureDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ConfigureDialog)

    def retranslateUi(self, ConfigureDialog):
        ConfigureDialog.setWindowTitle(QtGui.QApplication.translate("ConfigureDialog", "Configure - Zinc Data Source", None, QtGui.QApplication.UnicodeUTF8))
        self.dataLineEdit.setToolTip(QtGui.QApplication.translate("ConfigureDialog", "Maybe a combined element and node file", None, QtGui.QApplication.UnicodeUTF8))
        self.dataButton.setText(QtGui.QApplication.translate("ConfigureDialog", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setToolTip(QtGui.QApplication.translate("ConfigureDialog", "Maybe a combined element and node file", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("ConfigureDialog", "Data File:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ConfigureDialog", "Identifier:", None, QtGui.QApplication.UnicodeUTF8))

