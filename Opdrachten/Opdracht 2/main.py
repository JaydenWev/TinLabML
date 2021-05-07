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
class Node: # base node
    def __init__(self):
        self.inputEdges = []
        self.outputEdges = []

    def sigmoid(self, x):
        # print(1 / (1 + mt.exp(-x)))
        return  1 / (1 + mt.exp(-x))

class BeginNode(Node): # inputNodes
    def __init__(self):
        self.value = 0
        self.inputEdges = []
        self.outputEdges = []

    def setValue(self,value):
        self.value = value

    
    def getValue(self):
        return self.sigmoid(self.value)

class NetworkNode(Node): # outputNodes

    
    def getValue(self):
        temp = 0
        for inputEdge in self.inputEdges:
            temp += self.sigmoid(inputEdge.getValue()) # ERROR in de getValue returned iets van het type Edge
        return temp


class Edge: # Edge
    def __init__(self):
        self.amplification = 1
        self.inputNode = None
        self.outputNode = None
        
    def getValue(self):
        return self.inputNode.getValue() * self.amplification
        
    def addAmplification(self, amplification):
        self.amplification += amplification
        




class Network:
    def __init__(self,trainingSets):
        self.trainingSets = trainingSets
        self.inputNodes = []
        self.outputNodes = []
        self.nodesInOutputLayer = 2
        #self.netWorkNode = NetworkNode()
    
    def createNetwork(self):
        for x in range(self.nodesInOutputLayer): # create output nodes
            self.outputNodes.append(NetworkNode())
        for x in range(len(trainingSets[0])): # create input nodes
            self.inputNodes.append(BeginNode())
            for y in range(self.nodesInOutputLayer):
                edge = Edge()
                self.inputNodes[x].inputEdges.append(edge)
                edge.inputNode = self.inputNodes[x]          # set edges input
                edge.outputNode = self.outputNodes[y]        # set edges output
                self.outputNodes[y].inputEdges.append(edge)  # set edge as input for output node
    
    def putSpecificSetInBeginNode(self,index):
        x = 0
        for value in trainingSets[index]:
            self.inputNodes[x].setValue(value)
            #print(value)
            x += 1
            
    
    def getValueOutputNodes(self):
        ValueOutputNodes = []
        for x in range(self.nodesInOutputLayer):
            ValueOutputNodes.append(self.outputNodes[x].getValue())
            
        #print(ValueOutputNodes)
        return ValueOutputNodes
        
    def normalize(self,index):
        self.putSpecificSetInBeginNode(index)
        vector = self.getValueOutputNodes()
        factor = mt.sqrt(mt.pow(vector[0],2) + mt.pow(vector[1],2)) #sqaures the two values and take the sqrt from items
        vector[0] /= factor # take the quotient to normalize the vector
        vector[1] /= factor
        return vector # return the normalized vector
        
    def edgeLoop(self,amplifiedIndex, value):
        x = 0
        for outputNode in self.outputNodes:
            for inputEdge in outputNode.inputEdges:
                if amplifiedIndex == x:
                    inputEdge.addAmplification(value)
                    #print(inputEdge.amplification)
                x += 1
    
    def printEdges(self):
        for outputNode in self.outputNodes:
            for inputEdge in outputNode.inputEdges:
                    print(inputEdge.amplification)

    
    def calculateAmps (self):
       
        rand = random.randint(-10,10)/10
        errorArray = [None]*18
        print("Rand",rand)

        for k in range(18):
            self.edgeLoop(k,rand)
            #opslaan van error gebeuren            
            #errorArray[k] = self.calculateError(shape, x)
            for x in range(4):
                current_error = 0
                self.putSpecificSetInBeginNode(x)
                if x == 0 or x == 1:
                    shape = circle
                else:
                    shape = cross
                
                current_error += self.calculateError(shape, x)           
            current_error /= 4 

                
            if k == 0:
                error = current_error
                index = k
                amplification_value = rand
            else:
                if error > current_error:
                    error = current_error
                    index = k 
                    amplification_value = rand
                 
            #checken voor beste error
            self.edgeLoop(k,-rand)
            
        self.edgeLoop(index,amplification_value)
        return error
        
        
        
    def calculateError (self, shape, index):
        vector = self.normalize(index)
        return mt.sqrt(mt.pow(shape[0]-vector[0],2) + mt.pow(shape[1]-vector[1],2))
        

        
        
net = Network(trainingSets)
net.createNetwork()
#print(net.normalize(net.getValueOutputNodes(),3))

#net.edgeLoop(3,0)
net.calculateAmps()
#vec1 = [0.9,0.1]
while net.calculateAmps() > 0.1:
    print("bezig")
    
net.printEdges()
print("\n\n\n")

print(net.normalize(0))
print(net.normalize(1))
print(net.normalize(2))
print(net.normalize(3))

#print(net.calculateError(vec1, cross))

#print(random.randint(-10,10)/10)
#input array moeten meerdere arrays worden zodat het een hele trainingset wordt
#print (trainingSet.flatten())
