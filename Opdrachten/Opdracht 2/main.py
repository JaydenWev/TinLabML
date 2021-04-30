'''
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
'''
# Imports
import math as mt
import numpy as np
import itertools as it

# Matrices
cross_1 = np.array([[0, 1, 0],
                    [1, 1, 1],
                    [0, 1, 0]]) # "cross")

cross_2 = np.array([[1, 0, 1],
                    [0, 1, 0],
                    [1, 0, 1]]) # "cross")

circle_1 = np.array([[1, 1, 1],
                    [1, 0, 1],
                    [1, 1, 1]]) # "circle")

circle_2 = np.array([[0, 1, 0],
                    [1, 0, 1],
                    [0, 1, 0]]) # "circle")

# Classes defenition
class Node: # base node
    def __init__(self):
        self.inputEdges = []
        self.outputEdges = []

    def sigmoid(self, x):
        # print(1 / (1 + mt.exp(-x)))
        return  1 / (1 + mt.exp(-x))

class BeginNode(Node): # inputNodes
    def __init__(self,value):
        self.value = value
        self.inputEdges = []
        self.outputEdges = []

        
    def getValue(self):
        return self.sigmoid(self.value)

class NetworkNode(Node): # outputNodes
    temp = 0
    def getValue(self):
        for inputEdge in self.inputEdges:
            self.temp += self.sigmoid(inputEdge.getValue()) # ERROR in de getValue returned iets van het type Edge
            # print(self.temp)
        return self.temp

class Edge: # Edge
    def __init__(self):
        self.amplification = 1
        self.inputNode = None
        self.outputNode = None
        
    def getValue(self):
        return self.inputNode.getValue() * self.amplification

# Main code
inputNodes = []
outputNodes = []

nodesInLayer_1 = 9
nodesInOutputLayer = 2

def createNetwork(matrix):
    for x in range(nodesInOutputLayer): # create output nodes
        outputNodes.append(NetworkNode())

    for x in range(nodesInLayer_1): # create input nodes
        inputNodes.append(BeginNode(matrix[x]))
        for y in range(nodesInOutputLayer):
            edge = Edge()
            inputNodes[x].inputEdges.append(edge)
            edge.inputNode = inputNodes[x]          # set edges input
            edge.outputNode = outputNodes[y]        # set edges output
            outputNodes[y].inputEdges.append(edge)  # set edge as input for output node
# print (circle_1.flatten()[0])
createNetwork(circle_2.flatten()) # possibly easier to 'insert' list into the network into a function

#print(list(it.chain(*cross_1)), "\n")

print(outputNodes[0].getValue())
print(outputNodes[1].getValue())

