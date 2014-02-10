#!/usr/bin/python
"""
@brief DuinoRobot class for PcDuino
@author Sebastien TACK (sebastien.tack@ac-caen.fr) 
@date 10/02/2014 
@version: 1.0 
@copyright: Copyright (C) 2014, mrTForge see the LICENSE file included with this software (see LINENSE file)
"""

import os
import sys
import time
import math
import re
import socket
import threading
import numpy as np

from pyduino_pcduino import * # importe les fonctions Arduino pour Python


class DuinoRobot():
    """The DuinoRobot Class"""

    # === Class Properties ===

    MOTA1 = 1	
    MOTA2 = 2	
    MOTB1 = 3	
    MOTB2 = 4	

    # === Class Methods ===
    # Constructor
    def __init__(self, baseIP, robotIP):

        # Initialize GPIO pins
	"""
	self.port = 5000
        self.baseIP = baseIP
        self.robotIP = robotIP
        self.robotSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.robotSocket.setblocking(False)
        self.robotSocket.bind((self.robotIP, self.port))
	"""
    # Getters and Setters

    # Methods
    #configure ports and so
    def setup(self):
        pinMode(self.MOTA1,OUTPUT);
        pinMode(self.MOTA2,OUTPUT);
        pinMode(self.MOTB1,OUTPUT);
        pinMode(self.MOTB2,OUTPUT);
	#digitalWrite(self.pwmPin[LEFT],0);
	#digitalWrite(self.pwmPin[RIGHT],0);
        #self.setPWM([0, 0])
        #self.encoderRead = encoderRead(self.encoderPin)
        return

    #main method call from DuinoRobotRun.py script
    def run(self):
        self.setup()
        return


