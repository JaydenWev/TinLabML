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
        self.filePath = 'result.txt'
        self.sharedValues = fi.readFromFile(self.filePath)
        self.startTime = tm.process_time()
        self.looped = 0

        
        while True:
            self.timer.tick ()
            self.input ()
            self.sweep ()
            self.output ()
            self.sharedValues[0] = round(tm.process_time() - self.startTime, 2)
            # print('Time: ', self.sharedValues[0], 's')
            fi.writeToFile(self.filePath, self.sharedValues)
            tm.sleep (0.02)
            
    def sweep (self):   # Control algorithm to be tested
        self.nearestObstacleDistance = self.finity
        self.nearestObstacleAngle = 0
        
        self.nextObstacleDistance = self.finity 
        self.nextObstacleAngle = 0

        self.next2ObstacleDistance = self.finity
        self.next2ObstacleAngle = 0

        self.next3ObstacleDistance = self.finity
        self.next3ObstacleAngle = 0
        for lidarAngle in range (-self.lidarHalfApertureAngle, self.lidarHalfApertureAngle):
            lidarDistance = self.lidarDistances [lidarAngle]
            if(lidarDistance < 3):
                if lidarDistance < self.nearestObstacleDistance:
                    self.next3ObstacleDistance = self.next2ObstacleDistance
                    self.next3ObstacleAngle = self.next2ObstacleAngle

                    self.next2ObstacleDistance = self.nextObstacleDistance 
                    self.next2ObstacleAngle = self.nextObstacleAngle

                    self.nextObstacleDistance =  self.nearestObstacleDistance
                    self.nextObstacleAngle = self.nearestObstacleAngle
                    
                    self.nearestObstacleDistance = lidarDistance 
                    self.nearestObstacleAngle = lidarAngle

                elif lidarDistance < self.nextObstacleDistance:
                    self.next3ObstacleDistance = self.next2ObstacleDistance
                    self.next3ObstacleAngle = self.next2ObstacleAngle
                    
                    self.next2ObstacleDistance = self.nextObstacleDistance
                    self.next2ObstacleAngle = self.nextObstacleAngle

                    self.nextObstacleDistance = lidarDistance
                    self.nextObstacleAngle = lidarAngle


                elif lidarDistance < self.next2ObstacleDistance:
                    self.next3ObstacleDistance = self.next2ObstacleDistance
                    self.next3ObstacleAngle = self.next2ObstacleAngle

                    self.next2ObstacleDistance = lidarDistance
                    self.next2ObstacleAngle = lidarAngle


                elif lidarDistance < self.next3ObstacleDistance:
                    self.next3ObstacleDistance = lidarDistance
                    self.next3ObstacleAngle = lidarAngle
            if(self.looped < 3):
                self.targetObstacleDistance = (self.nearestObstacleDistance + self.nextObstacleDistance) / 2
                self.targetObstacleAngle = (self.nearestObstacleAngle + self.nextObstacleAngle) / 2
                self.looped += 1
            elif(self.looped == 3):
                self.targetObstacleDistance = (self.nearestObstacleDistance + self.nextObstacleDistance + self.next2ObstacleDistance + self.next3ObstacleDistance) / 4
                self.targetObstacleAngle = (self.nearestObstacleAngle + self.nextObstacleAngle + self.next2ObstacleAngle + self.next3ObstacleAngle) / 4
                self.looped = 0
            
            self.steeringAngle = self.steeringPidController.getY (self.timer.deltaTime, self.targetObstacleAngle, 0)
            self.targetVelocity = ((90 - abs (self.steeringAngle)) / 60) if self.driveEnabled else 0

        if self.physics.slipping() == True:
            self.amountOfSlip += 1 
            self.sharedValues[4] = self.amountOfSlip
   
        
        
        #bereken score van afgelopen baan
        #zet dit en pid in bestand
        #print(self.steeringPidController.getP(),self.steeringPidController.getI(),self.steeringPidController.getD())
