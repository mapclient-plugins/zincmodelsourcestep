"""
MAP Client, a program to generate detailed musculoskeletal models for OpenSim.
    Copyright (C) 2012  University of Auckland

This file is part of MAP Client. (http://launchpad.net/mapclient)

    MAP Client is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    MAP Client is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with MAP Client.  If not, see <http://www.gnu.org/licenses/>..
"""
import os

from PySide6.QtWidgets import QDialog, QFileDialog, QDialogButtonBox

from mapclientplugins.zincmodelsourcestep.ui_configuredialog import Ui_ConfigureDialog
from mapclientplugins.zincmodelsourcestep.zincmodeldata import ZincModelData

REQUIRED_STYLE_SHEET = 'border: 1px solid red; border-radius: 3px'
DEFAULT_STYLE_SHEET = ''


class ConfigureDialog(QDialog):
    """
    Configure dialog to present the user with the options to configure this step.
    """

    def __init__(self, parent=None):
        """
        Constructor
        """
        QDialog.__init__(self, parent)
        self._ui = Ui_ConfigureDialog()
        self._ui.setupUi(self)

        self._makeConnections()

    def _makeConnections(self):
        self._ui.elementButton.clicked.connect(self._elementButtonClicked)
        self._ui.nodeButton.clicked.connect(self._nodeButtonClicked)
        self._ui.elementLineEdit.textChanged.connect(self.validate)
        self._ui.nodeLineEdit.textChanged.connect(self.validate)
        self._ui.identifierLineEdit.textChanged.connect(self.validate)

    def setState(self, state):
        self._ui.identifierLineEdit.setText(state._identifier)
        self._ui.elementLineEdit.setText(state._elementLocation)
        self._ui.nodeLineEdit.setText(state._nodeLocation)

    def getState(self):
        state = ZincModelData()
        state._identifier = self._ui.identifierLineEdit.text()
        state._elementLocation = self._ui.elementLineEdit.text()
        state._nodeLocation = self._ui.nodeLineEdit.text()

        return state

    def validate(self):
        identifier_valid = len(self._ui.identifierLineEdit.text()) > 0
        if identifier_valid:
            self._ui.identifierLineEdit.setStyleSheet(DEFAULT_STYLE_SHEET)
        else:
            self._ui.identifierLineEdit.setStyleSheet(REQUIRED_STYLE_SHEET)

        element_valid = len(self._ui.elementLineEdit.text()) > 0
        if element_valid:
            self._ui.elementLineEdit.setStyleSheet(DEFAULT_STYLE_SHEET)
        else:
            self._ui.elementLineEdit.setStyleSheet(REQUIRED_STYLE_SHEET)

        valid = identifier_valid and element_valid
        self._ui.buttonBox.button(QDialogButtonBox.StandardButton.Ok).setEnabled(valid)

        return valid

    def _lineEditFile(self, line_edit):
        (fileName, _) = QFileDialog.getOpenFileName(self, 'Select Zinc File', self._ui.previousLocationLabel.text())

        if fileName:
            location = os.path.basename(fileName)
            self._ui.previousLocationLabel.setText(location)
            line_edit.setText(fileName)

        self.validate()

    def _elementButtonClicked(self):
        self._lineEditFile(self._ui.elementLineEdit)

    def _nodeButtonClicked(self):
        self._lineEditFile(self._ui.nodeLineEdit)
