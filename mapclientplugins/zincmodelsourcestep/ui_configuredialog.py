# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'configuredialog.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_ConfigureDialog(object):
    def setupUi(self, ConfigureDialog):
        if not ConfigureDialog.objectName():
            ConfigureDialog.setObjectName(u"ConfigureDialog")
        ConfigureDialog.resize(593, 253)
        self.verticalLayout_2 = QVBoxLayout(ConfigureDialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox = QGroupBox(ConfigureDialog)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.identifierLineEdit = QLineEdit(self.groupBox)
        self.identifierLineEdit.setObjectName(u"identifierLineEdit")

        self.gridLayout.addWidget(self.identifierLineEdit, 0, 1, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.elementLineEdit = QLineEdit(self.groupBox)
        self.elementLineEdit.setObjectName(u"elementLineEdit")
        self.elementLineEdit.setStyleSheet(u"selection-color: red;\n"
"color: green")

        self.horizontalLayout.addWidget(self.elementLineEdit)

        self.elementButton = QPushButton(self.groupBox)
        self.elementButton.setObjectName(u"elementButton")
        font = QFont()
        font.setBold(True)
        self.elementButton.setFont(font)

        self.horizontalLayout.addWidget(self.elementButton)


        self.gridLayout.addLayout(self.horizontalLayout, 1, 1, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(71, 0))

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(71, 0))

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.nodeLineEdit = QLineEdit(self.groupBox)
        self.nodeLineEdit.setObjectName(u"nodeLineEdit")
        self.nodeLineEdit.setStyleSheet(u"selection-color: red;\n"
"color: green")

        self.horizontalLayout_3.addWidget(self.nodeLineEdit)

        self.nodeButton = QPushButton(self.groupBox)
        self.nodeButton.setObjectName(u"nodeButton")
        self.nodeButton.setFont(font)

        self.horizontalLayout_3.addWidget(self.nodeButton)


        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 1, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 3, 1, 1, 1)

        self.previousLocationLabel = QLabel(self.groupBox)
        self.previousLocationLabel.setObjectName(u"previousLocationLabel")
        self.previousLocationLabel.setMaximumSize(QSize(0, 16777215))

        self.gridLayout.addWidget(self.previousLocationLabel, 4, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.buttonBox = QDialogButtonBox(ConfigureDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout_2.addWidget(self.buttonBox)

#if QT_CONFIG(shortcut)
        self.label_3.setBuddy(self.elementLineEdit)
        self.label_4.setBuddy(self.elementLineEdit)
        self.label.setBuddy(self.identifierLineEdit)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(ConfigureDialog)
        self.buttonBox.accepted.connect(ConfigureDialog.accept)
        self.buttonBox.rejected.connect(ConfigureDialog.reject)

        QMetaObject.connectSlotsByName(ConfigureDialog)
    # setupUi

    def retranslateUi(self, ConfigureDialog):
        ConfigureDialog.setWindowTitle(QCoreApplication.translate("ConfigureDialog", u"Configure - Zinc Model Source", None))
        self.groupBox.setTitle("")
#if QT_CONFIG(tooltip)
        self.elementLineEdit.setToolTip(QCoreApplication.translate("ConfigureDialog", u"Maybe a combined element and node file", None))
#endif // QT_CONFIG(tooltip)
        self.elementButton.setText(QCoreApplication.translate("ConfigureDialog", u"...", None))
#if QT_CONFIG(tooltip)
        self.label_3.setToolTip(QCoreApplication.translate("ConfigureDialog", u"Maybe a combined element and node file", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("ConfigureDialog", u"Element File:", None))
        self.label_4.setText(QCoreApplication.translate("ConfigureDialog", u"Node File:", None))
        self.nodeButton.setText(QCoreApplication.translate("ConfigureDialog", u"...", None))
        self.label.setText(QCoreApplication.translate("ConfigureDialog", u"Identifier:", None))
        self.previousLocationLabel.setText("")
    # retranslateUi

