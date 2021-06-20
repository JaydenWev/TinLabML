import subprocess
import sys
import time

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
    sys.exit()

def restart() :
    global p
    p.terminate()
    #time.sleep()
    p = subprocess.Popen("py world.py")
    emptyFile()
    calculatePID()

    
def emptyFile():
    f = open("command.txt", "w")
    f.write("empty")
    f.close()


    
while(1):
    time.sleep(1)
    f = open("command.txt", "r")
    action = f.read()
    if(action == "restart"):
        f.close()
        restart()
    elif(action == "stop"):
        f.close()
        stop()
    elif(action == "start"):
        f.close()
        start()
    else:
        f.close()
    





#while(1):
#    pass

#sys.exit()
