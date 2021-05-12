'''
Bob, Boyd, Jayden, Keanu
Prioritized requirements
    Input is een 2d matrix

Main design choices


Test specification

TO DO
1. inputNodes pakken een waarde van de matric en gooien die door de sigmoid()
2. waarde gaat door edge en wordt geamplified
3. in netwerkNode gaat de waarde door de sigmoid

de netwerkNodes die pakken de waarde van de inputNodes
    in de edges worden de waardes gemultiplied met de amplification

   Return value is een recusieve functie
   Nodes overerven
   
   
   circle = [0,1]
   cross = [1,0]
   
'''
# Imports
import math as mt
import numpy as np
import itertools as it
import random
circle = [0,1]
cross = [1,0]
# Matrices
cross_1 = np.array([[0, 1, 0],
                    [1, 1, 1],
                    [0, 1, 0]]) # "cross")

cross_2 = np.array([[1, 0, 1],
                    [0, 1, 0],
                    [1, 0, 1]]) # "cross")

circle_1 =np.array([[1, 1, 1],
                    [1, 0, 1],
                    [1, 1, 1]]) # "circle")

circle_2 =np.array([[0, 1, 0],
                    [1, 0, 1],
                    [0, 1, 0]]) # "circle")

trainingSets = np.array([cross_1.flatten(),cross_2.flatten(),circle_1.flatten(),circle_2.flatten()])

# Classes defenition
class Node: # Base node
    def __init__(self):
        self.inputEdges = []
        self.outputEdges = []

    def sigmoid(self, x):
        # print(1 / (1 + mt.exp(-x)))
        return  1 / (1 + mt.exp(-x))

class BeginNode(Node): # InputNodes
    def __init__(self):
        self.value = 0
        self.inputEdges = []
        self.outputEdges = []

    def setValue(self,value):
        self.value = value

    
    def getValue(self):
        return self.sigmoid(self.value)

class NetworkNode(Node): # OutputNodes

    
    def getValue(self):
        temp = 0
        for inputEdge in self.inputEdges:
            temp += inputEdge.getValue()
        return self.sigmoid(temp)


class Edge: # Edge
    def __init__(self):
        self.amplification = 1
        self.inputNode = None
        self.outputNode = None
        
    def getValue(self):
        return (self.inputNode.getValue() * self.amplification)
        
    def addAmplification(self, amplification):
        self.amplification += amplification
        




class Network:
    def __init__(self,trainingSets):
        self.trainingSets = trainingSets
        self.inputNodes = []
        self.outputNodes = []
        self.nodesInOutputLayer = 2
        # self.netWorkNode = NetworkNode()
        
    
    def createNetwork(self):
        for iOutput in range(self.nodesInOutputLayer): # Create output nodes
            self.outputNodes.append(NetworkNode())
            
        for iInput in range(len(trainingSets[0])): # Create input nodes
            self.inputNodes.append(BeginNode())
            for iOutput in range(self.nodesInOutputLayer):
                edge = Edge()
                self.inputNodes[iInput].outputEdges.append(edge)
                edge.inputNode = self.inputNodes[iInput]          # Set edges input
                edge.outputNode = self.outputNodes[iOutput]        # Set edges output
                self.outputNodes[iOutput].inputEdges.append(edge)  # Set edge as input for output node
    
    def putSpecificMatrixInBeginNode(self,index):
        for iInput, value in enumerate (self.trainingSets[index]):
            self.inputNodes[iInput].setValue(value)

    def putSpecificSetInBeginNodeUsingArray(self,array):
        for iInput, value in enumerate(array):
            self.inputNodes[iInput].setValue(value)
    
    def getValueOutputNodes(self):
        valueOutputNodes = []
        for iOutput in range(self.nodesInOutputLayer):
            valueOutputNodes.append(self.outputNodes[iOutput].getValue())

        return valueOutputNodes
        
    def normalize(self,index):
        self.putSpecificMatrixInBeginNode(index)
        vector = self.getValueOutputNodes()
        factor = mt.sqrt(mt.pow(vector[0],2) + mt.pow(vector[1],2)) # Sqaures the two values and take the sqrt from items
        # print("index",index)
        # print("voor",vector)
        vector[0] /= factor # take the quotient to normalize the vector
        vector[1] /= factor

        # print(vector)
        # print(index)
        return vector # return the normalized vector

    def normalize2(self,array):
        self.putSpecificSetInBeginNodeUsingArray(array)
        vector = self.getValueOutputNodes()
        factor = mt.sqrt(mt.pow(vector[0],2) + mt.pow(vector[1],2)) # Sqaures the two values and take the sqrt from items
        # print("index",index)
        # print("voor",vector)
        vector[0] /= factor # take the quotient to normalize the vector
        vector[1] /= factor
        # print(vector)
        # print(index)
        return vector # return the normalized vector
        
    def addAmplificationOnIndex(self,amplifiedIndex, value):
        iEdge = 0
        #for inputEdge in outputNode.inputEdges:
         #   for outputNode in self.outputNodes:
        for inputNode in self.inputNodes:
            for outputEdge in inputNode.outputEdges:
                if amplifiedIndex == iEdge:
                    outputEdge.addAmplification(value)
                    return
                    # print(inputEdge.amplification)
                iEdge += 1
    
    def printEdges(self):
        print("######\tBEGIN EDGES\t######")
        for inputNode in self.inputNodes:
            for outputEdge in inputNode.outputEdges:
                    print(outputEdge.amplification)
        print("######\tEND EDGES\t######")

    
    def calculateAmps (self):
        rand = random.randint(-10,10)/10
        errorArray = [None]*18

        # print("Rand:",rand)

        for iEdge in range(18):
            self.addAmplificationOnIndex(iEdge,rand) # Opslaan van error gebeuren            
            current_error = 0  
            for iTrainingSetElement in range(4):
                
                self.putSpecificMatrixInBeginNode(iTrainingSetElement)
                if iTrainingSetElement in {0,1}:
                    shape = circle
                else:
                    shape = cross
                # ErrorArray[k] = self.calculateError(shape, x)
                current_error += self.calculateError(shape, iTrainingSetElement)
           # print ()
          #  print('-+-',self.calculateError(shape, iTrainingSetElement))
          #  print('-+-',current_error)
          #  print()
            current_error /= 4 # Gemiddelde error over de 4 matrices
            errorArray[iEdge] = current_error

            self.addAmplificationOnIndex(iEdge,-rand) # Reset de amplification
     
        lowestErrorIndex = errorArray.index(min(errorArray))
        self.addAmplificationOnIndex(lowestErrorIndex, rand)
        #print ('*', min(errorArray))
        return min(errorArray)
        
        #min(errorArray)
        
    def calculateError (self, shape, iSetElement):
        vector = self.normalize(iSetElement)
        #print(vector[0],vector[1])
        a = mt.sqrt(mt.pow(shape[1]-vector[0],2) + mt.pow(shape[0]-vector[1],2))
        #print(self.normalize(iSetElement), '---', a)
        return a
        

        
        
net = Network(trainingSets)
net.createNetwork()
#print(net.normalize(net.getValueOutputNodes(),3))

#net.edgeLoop(3,0)
#net.calculateAmps()
#vec1 = [0.9,0.1]
while net.calculateAmps() > 0.01:
    pass
    
net.printEdges()
print("\n\n\n")

print(net.normalize(0))
print(net.normalize(1))
print(net.normalize(2))
print(net.normalize(3))




testArray =np.array([[1, 0, 1],
                    [0, 1, 0],
                    [0, 0, 1]]).flatten()

print (net.normalize2(testArray))

#print(net.calculateError(vec1, cross))

#print(random.randint(-10,10)/10)
#input array moeten meerdere arrays worden zodat het een hele trainingset wordt
#print (trainingSet.flatten())
