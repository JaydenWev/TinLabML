import subprocess
import sys
import time
import random
import FileInteractorJSON as fi
bestValues = [94.73, 1.05, 0, -0.03, 1287]
p = subprocess.Popen("py world.py")
resultPath = "result.txt"

print("process started")

#p = subprocess.Popen("py runCode.py")

def calculatePID():
    pass

def start() :
    global p
    p = subprocess.Popen("py world.py")
    print("RunCode started world py")
    emptyFile()

def forceStop() :
    global p
    p.terminate()
    emptyFile()
    print("process stopped")


    line = fi.readFromFile(resultPath)
    line[0]=1000
    fi.writeToFile(resultPath, line)

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
currentPid = readPid()
previousPid = currentPid
i = 0
previousTime = fi.readFromFile(resultPath)[0]
print("previousTime: ", previousTime)
while(1):
    time.sleep(1)
    f = open("command.txt", "r")
    action = f.read()
    f.close()
    if(action == "restart"):        #nog checken of waarde idd verbeterd
        file = fi.readFromFile(resultPath)

        #previous is the run that has been done with the fastest time
        #mutated is the pid that has been randomly changed
        
        if(int(file[0]) > previousTime):     #when not improved
            currentPid = previousPid
        else:
            previousPid = readPid()
            
        if (i == 0):    #&& file[0] < previousTime
            currentPid[0] = float(previousPid[0]) + random.randint(-10, 10)/100
            i =+ 1
        elif(i == 1):
            currentPid[1] = float(previousPid[1]) + random.randint(-10, 10)/100
            i =+ 1
        elif(i == 2):
            currentPid[2] = float(previousPid[2]) + random.randint(-10, 10)/100
            i = 0
        print("Previous pid before write",previousPid)
        writePid(currentPid)
        restart()
        #previousPid = readPid()
        
    elif(action == "stop"):
        forceStop()
    elif(action == "start"):
        start()
    
    #random.randint(-10, 10)/100
    
    





#while(1):
#    pass

#sys.exit()