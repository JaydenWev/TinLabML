# ====== Legal notices
#
# Copyright (C) 2013 - 2020 GEATEC engineering
#
# This program is free software.
# You can use, redistribute and/or modify it, but only under the terms stated in the QQuickLicence.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY, without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the QQuickLicence for details.
#
# The QQuickLicense can be accessed at: http://www.geatec.com/qqLicence.html
#
# __________________________________________________________________________
#
#
#  THIS PROGRAM IS FUNDAMENTALLY UNSUITABLE FOR CONTROLLING REAL SYSTEMS !!
#
# __________________________________________________________________________
#
# It is meant for training purposes only.
#
# Removing this header ends your licence.
#

import simpylc as sp
import lidar_pilot_scada_io as ls
import sys
class LidarPilotSimulatedIo (ls.LidarPilotScadaIo):
    def __init__ (self):
        self.world = sp.world
        print ('Use down arrow to restart, up arrow to stop')
        self.finity = sp.finity
        super () .__init__ ()
        
        
    def input (self):   # Input from simulator
        super () .input ()
        key = sp.getKey ()
        
        #if key == 'KEY_UP':
        self.driveEnabled = True
        if key == 'KEY_DOWN':
            #self.driveEnabled = False
            f = open("command.txt", "w")
            f.write("restart")
            f.close()
        elif key == 'KEY_UP':
            #self.driveEnabled = False
            f = open("command.txt", "w")
            f.write("stop")
            f.close()
        
        self.lidarDistances = sp.world.visualisation.lidar.distances
        self.lidarHalfApertureAngle = sp.world.visualisation.lidar.halfApertureAngle
        
    def output (self):  # Output to simulator
        super () .output ()
        sp.world.physics.steeringAngle.set (self.steeringAngle)
        sp.world.physics.targetVelocity.set (self.targetVelocity)
    
    
       
