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
__version__ = '0.1.0'
__author__ = 'Hugh Sorby'

import os, sys

current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    # Using __file__ will not work if py2exe is used,
    # Possible problem of OSX10.6 also.
    sys.path.insert(0, current_dir)

# import class that derives itself from the step mountpoint.
<<<<<<< HEAD
import zincmodelsourcestep.widgets.resources_rc
from zincmodelsourcestep import step
=======
import zincdatasourcestep.widgets.resources_rc
from zincdatasourcestep import step
>>>>>>> 1d501d9f22afbba3a59243f382f3c58e9d133db2

( _, tail ) = os.path.split(current_dir)
print("Plugin '{0}' version {1} by {2} loaded".format(tail, __version__, __author__))
