import numpy as np

emptyMatrix = np.array([[0, 0, 0],
                    [0, 0, 0],
                    [0, 0, 0], ]) # "empty")
print(emptyMatrix)
print(type(emptyMatrix))

np.savetxt("emptyMatrix.csv", emptyMatrix, delimiter=",")

myFile = np.genfromtxt('emptyMatrix.csv', delimiter=',')
print("\n\n", myFile)
print(type(myFile))




# ###################################################################
# ###################################################################
# Place below in main.py                          ###################



def storeEdgesInFile(self):
    valuesToStore = []
    for outputNode in self.outputNodes:
        for inputEdge in outputNode.inputEdges:
                valuesToStore.append(inputEdge.amplification)
    np.savetxt("storedValues.csv", valuesToStore, delimiter=",")

def readEdgesFromFile(self):
    return np.genfromtxt('storedValues.csv', delimiter=',')

def setEdgesAmplificationFromFile(self):
    fromFile = self.readEdgesFromFile()
    fileCounter = 0
    for outputNode in self.outputNodes:
        for inputEdge in outputNode.inputEdges:
            inputEdge.setAmplification(fromFile)
            fileCounter += 1
