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
import time as tm
import traceback as tb
import math as mt

import timer as tr
import pid_controller as pc
import error_value as ev

import FileInteractorJSON as fi

class LidarPilotBase:
    def __init__ (self):
        self.physics = ev.ErrorValue(self.world)
        self.driveEnabled = False
        self.steeringAngle = 0
        self.amountOfSlip = 0
        self.timer = tr.Timer ()
        
        ##
        f = open("PIDvalues.txt", "r")
        line = f.read()
        f.close()
        currentline = line.split(",")
        #total = str(currentline[0] + currentline[1] + currentline [2]) + "\n"
        #PIDvalues
        print("PID VALUES FROM FILE: ", currentline[0] , currentline[1] , currentline [2])
        ##kies pid waarde afhankelijk van voorgaande versies
        ##
        self.steeringPidController = pc.PidController (float(currentline[0]), float(currentline[1]), float(currentline[2]))
        self.filePath = 'test.txt'
        self.sharedValues = fi.readFromFile(self.filePath)
        self.startTime = tm.process_time()
        while True:
            self.timer.tick ()
            self.input ()
            self.sweep ()
            self.output ()
            self.sharedValues[0] = round(tm.process_time() - self.startTime, 2)
            print('Time: ', self.sharedValues[0], 's')
            fi.writeToFile(self.filePath, self.sharedValues)
            tm.sleep (0.02)
            
    def sweep (self):   # Control algorithm to be tested
        
        
        self.nearestObstacleDistance = self.finity
        self.nearestObstacleAngle = 0
        
        self.nextObstacleDistance = self.finity
        self.nextObstacleAngle = 0

        for lidarAngle in range (-self.lidarHalfApertureAngle, self.lidarHalfApertureAngle):
            lidarDistance = self.lidarDistances [lidarAngle]
            
            if lidarDistance < self.nearestObstacleDistance:
                self.nextObstacleDistance =  self.nearestObstacleDistance
                self.nextObstacleAngle = self.nearestObstacleAngle
                
                self.nearestObstacleDistance = lidarDistance 
                self.nearestObstacleAngle = lidarAngle

            elif lidarDistance < self.nextObstacleDistance:
                self.nextObstacleDistance = lidarDistance
                self.nextObstacleAngle = lidarAngle
           
        self.targetObstacleDistance = (self.nearestObstacleDistance + self.nextObstacleDistance) / 2
        self.targetObstacleAngle = (self.nearestObstacleAngle + self.nextObstacleAngle) / 2
        
        self.steeringAngle = self.steeringPidController.getY (self.timer.deltaTime, self.targetObstacleAngle, 0)
        self.targetVelocity = ((90 - abs (self.steeringAngle)) / 60) if self.driveEnabled else 0

        if self.physics.slipping() == True:
            self.amountOfSlip += 1 
            self.sharedValues[4] = self.amountOfSlip
   
        
        
        #bereken score van afgelopen baan
        #zet dit en pid in bestand
        #print(self.steeringPidController.getP(),self.steeringPidController.getI(),self.steeringPidController.getD())
