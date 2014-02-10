#!/usr/bin/python
"""
@brief Run QuickBot class for Beaglebone Black

@author Rowland O'Flaherty (rowlandoflaherty.com)
@date 02/07/2014
@version: 1.0
@copyright: Copyright (C) 2014, Georgia Tech Research Corporation see the LICENSE file included with this software (see LINENSE file)
"""

import sys
import time
from DuinoRobot import *

print "Running DuinoRobot"

baseIP = '192.168.7.1'
robotIP = '192.168.7.2'

if len(sys.argv) > 3:
    print 'Invalid number of command line arguments.'
    print 'Proper syntax:'
    print '>> DuinoRobotRun.py baseIP robotIP'
    print 'Example:'
    print '>> DuinoRobotRun.py ', baseIP, ' ', robotIP
    sys.exit()

if len(sys.argv) >= 2:
    baseIP = sys.argv[1]

if len(sys.argv) >= 3:
    robotIP = sys.argv[2]

print 'Running DuinoRobot Program'
print '    Base IP: ', baseIP
print '    Robot IP: ', robotIP

DR = DuinoRobot(baseIP, robotIP)
DR.run()
