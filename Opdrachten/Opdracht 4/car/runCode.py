import subprocess
import sys
import time
import random
testvalue1 = [84.73, 1.05, 0, -0.03, 1287]
testvalue2 = [83.73, 1.03, 0, -0.04, 1287]
testvalue3 = [82.73, 1.03, 0, -0.03, 1287]
testvalue4 = [81.73, 1.01, 0, -0.05, 1287]
p = subprocess.Popen("py world.py")

print("process started")

#p = subprocess.Popen("py runCode.py")

def calculatePID():
    pass

def start() :
    global p
    p = subprocess.Popen("py world.py")
    print("RunCode started world py")
    emptyFile()
    
def stop() :
    global p
    p.terminate()
    emptyFile()
    print("process stopped")
    sys.exit()

def restart() :
    global p
    p.terminate()
    #time.sleep()
    print("subprocess restarted")
    p = subprocess.Popen("py world.py")
    emptyFile()
    calculatePID()

    
def emptyFile():
    f = open("command.txt", "w")
    f.write("empty")
    f.close()

def readPid():    
    f = open("PIDvalues.txt", "r")
    previousPid = f.read()
    f.close()
    previousPid = previousPid.split(",")
    print("PID VALUES FROM FILE: ", previousPid[0] , previousPid[1] , previousPid [2])
    return previousPid

def writePid(pid):    
    f = open("PIDvalues.txt", "w")
    string = str(pid[0])+","+str(pid[1])+","+str(pid[2])
    f.write(string)
    f.close()

#total = str(currentline[0] + currentline[1] + currentline [2]) + "\n"
#PIDvalues
previousPid = readPid()
i = 0
while(1):
    time.sleep(1)
    f = open("command.txt", "r")
    action = f.read()
    f.close()
    if(action == "restart"):        #nog checken of waarde idd verbeterd
        if (i == 0):
            previousPid[0] = float(previousPid[0]) + random.randint(-10, 10)/100
            i =+ 1
        elif(i == 1):
            previousPid[1] = float(previousPid[1]) + random.randint(-10, 10)/100
            i =+ 1
        elif(i == 2):
            previousPid[2] = float(previousPid[2]) + random.randint(-10, 10)/100
            i = 0
        print("precvious pid before write",previousPid)
        writePid(previousPid)
        restart()
        previousPid = readPid()
        
    elif(action == "stop"):
        stop()
    elif(action == "start"):
        start()
    
    #random.randint(-10, 10)/100
    
    





#while(1):
#    pass

#sys.exit()
