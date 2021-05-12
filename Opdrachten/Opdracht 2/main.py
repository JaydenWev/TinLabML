'''
Bob, Boyd, Jayden, Keanu

This can be done by first creating inputnodes which represent the input values of a trainingSet. A neural network
also requires output nodes which describe the output using either a zero, one or a combination.

Prioritized requirements
    Input using 2d matrix
    dependent on the matrix the output should look closely like the following vector: [0,1] for a circle and [1,0] for a cross

Main design choices
    • A function should never have more then one function stated in plain code
      Therefore if a function needs to perform multiple tasks other functin should be nested within
    • The network must be created before inserting a training/test-set
    • All neural network functions should be in the appropriate class
    • The different types of nodes should inherit their base functions from a base Node class


Test specification
    1. Insert a test set using the amplification result of the trainingSet.
        Passed: The neural net recognises wich matrix is simular to a cross/shape
        Fail: The neural net does not recognise corectly which matrix is a cross/shape
    2. Insert a matrix that is close the trainingSet but not the same
        Passed: The neural net still recognises wich matrix is simular to a cross/shape with a slight decrease in cofindence
        Fail: The neural net does not recognise corectly which matrix is a cross/shape
    3. Insert a matrix that consist of only a single one in the middle, surrounded by zero's
        Passed: The neural net shows a low confidence 
        Fail: The neural net still recognizes a shape even if its not close to the trainingSet
Results:

       1. Passed
       2. Passed
       3. Passed

   
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
        vector[0] /= factor # take the quotient to normalize the vector
        vector[1] /= factor
        return vector # return the normalized vector

    def normalizeTestArray(self,array):
        self.putSpecificSetInBeginNodeUsingArray(array)
        vector = self.getValueOutputNodes()
        factor = mt.sqrt(mt.pow(vector[0],2) + mt.pow(vector[1],2)) # Sqaures the two values and take the sqrt from items
        vector[0] /= factor # take the quotient to normalize the vector
        vector[1] /= factor
        return vector # return the normalized vector
        
    def addAmplificationOnIndex(self,amplifiedIndex, value):
        iEdge = 0
        for inputNode in self.inputNodes:
            for outputEdge in inputNode.outputEdges:
                if amplifiedIndex == iEdge:
                    outputEdge.addAmplification(value)
                    return
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


        for iEdge in range(18):
            self.addAmplificationOnIndex(iEdge,rand) # Storing error value            
            current_error = 0  
            for iTrainingSetElement in range(4):
                
                self.putSpecificMatrixInBeginNode(iTrainingSetElement)
                if iTrainingSetElement in {0,1}:
                    shape = circle
                else:
                    shape = cross
                current_error += self.calculateError(shape, iTrainingSetElement)
            current_error /= 4 # Average error over 4 matrices
            errorArray[iEdge] = current_error

            self.addAmplificationOnIndex(iEdge,-rand) # Reset the amplification
     
        lowestErrorIndex = errorArray.index(min(errorArray))
        self.addAmplificationOnIndex(lowestErrorIndex, rand)
        return min(errorArray)

        
    def calculateError (self, shape, iSetElement):
        vector = self.normalize(iSetElement)
        a = mt.sqrt(mt.pow(shape[1]-vector[0],2) + mt.pow(shape[0]-vector[1],2))
        return a
        

        
        
net = Network(trainingSets)     #making a netwerk using the trainingset
net.createNetwork()         

while net.calculateAmps() > 0.01:
    pass
    
net.printEdges()    #prints amplifications of each edge
print("\nTraining results:")

print(net.normalize(0)) #prints the end result of the ouputnode
print(net.normalize(1))
print(net.normalize(2))
print(net.normalize(3))



print("\nTesting results:")
testArray_1 =np.array([[1, 0, 1],
                       [0, 1, 0],
                       [0, 0, 1]]).flatten()

testArray_2 =np.array([[0, 0, 1],
                       [0, 1, 0],
                       [1, 0, 0]]).flatten()

testArray_3 =np.array([[1, 1, 1],
                       [1, 0, 0],
                       [0, 1, 1]]).flatten()

testArray_4 =np.array([[0, 1, 0],
                       [0, 0, 1],
                       [0, 1, 0]]).flatten()

print (net.normalizeTestArray(testArray_1))
print (net.normalizeTestArray(testArray_2))
print (net.normalizeTestArray(testArray_3))
print (net.normalizeTestArray(testArray_4))
