import subprocess
import sys
import time

p = subprocess.Popen("py world.py")

print("process started")

#p = subprocess.Popen("py runCode.py")


def start() :
    global p
    p = subprocess.Popen("py world.py")
    print("RunCode started world py")
def stop() :
    global p
    p.terminate()
    sys.exit()

def restart() :
    global p
    p.terminate()
    #time.sleep()
    p = subprocess.Popen("py world.py")
    emptyFile()
def emptyFile():
    f = open("command.txt", "w")
    f.write("empty")
    f.close()
while(1):
    time.sleep(1)
    f = open("command.txt", "r")
    if(f.read() == "restart"):
        f.close()
        restart()
    else:
        f.close()
    

#while(1):
#    pass

#sys.exit()
