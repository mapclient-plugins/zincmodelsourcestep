'''
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
'''
import os

from PySide import QtCore, QtGui

from mountpoints.workflowstep import WorkflowStepMountPoint

from zincmodelsourcestep.widgets.configuredialog import ConfigureDialog
from zincmodelsourcestep.zincmodeldata import ZincModelData

class ZincModelSourceStep(WorkflowStepMountPoint):
    '''
    Zinc model source step supplies zinc model source files
    from a location on disk.
    '''
    
    def __init__(self, location):
        super(ZincModelSourceStep, self).__init__('Zinc Model Source', location)
        self._state = ZincModelData()
        self._icon = QtGui.QImage(':/zincmodelsource/images/zinc_model_icon.png')
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port', 'http://physiomeproject.org/workflow/1.0/rdf-schema#provides', 'http://physiomeproject.org/workflow/1.0/rdf-schema#zincmodel'))
        
    def configure(self):
        d = ConfigureDialog(self._state)
        d.setModal(True)
        if d.exec_():
            self._state = d.getState()
            self.serialize(self._location)
            
        self._configured = d.validate()
        if self._configured and self._configuredObserver:
            self._configuredObserver()
    
    def getIdentifier(self):
        return self._state._identifier
     
    def setIdentifier(self, identifier):
        self._state._identifier = identifier
     
    def serialize(self, location):
        configuration_file = os.path.join(location, getConfigFilename(self._state._identifier))
        s = QtCore.QSettings(configuration_file, QtCore.QSettings.IniFormat)
        s.beginGroup('state')
        s.setValue('identifier', self._state._identifier)
        s.setValue('element', self._state._elementLocation)
        s.setValue('node', self._state._nodeLocation)
        s.endGroup()
     
    def deserialize(self, location):
        configuration_file = os.path.join(location, getConfigFilename(self._state._identifier))
        s = QtCore.QSettings(configuration_file, QtCore.QSettings.IniFormat)
        s.beginGroup('state')
        self._state._identifier = s.value('identifier', '')
        self._state._elementLocation = s.value('element', '')
        self._state._nodeLocation = s.value('node', '')
        s.endGroup()
        d = ConfigureDialog(self._state)
        self._configured = d.validate()
        
    def portOutput(self):
        return self._state
     
def getConfigFilename(identifier):
    return identifier + '.conf'

