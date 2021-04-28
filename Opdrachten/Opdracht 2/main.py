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
import itertools as it

# Matrices
cross_1 = ([0, 1, 0],
            [1, 1, 1],
            [0, 1, 0], "cross")

cross_2 = ([1, 0, 1],
            [0, 1, 0],
            [1, 0, 1], "cross")

circle_1 = ([1, 1, 1],
            [1, 0, 1],
            [1, 1, 1], "circle")

circle_2 = ([0, 1, 0],
            [1, 0, 1],
            [0, 1, 0], "circle")

# Classes
class Node: # base node
    def __init__(self):
        self.inputEdges = []
        self.outputEdges = []

    def sigmoid(self, x):
        return  1 / (1 + mt.exp(-x))

class BeginNode(Node): # inputNodes
    def __init__(self, id, matrix):
        self.inputEdges = []
        self.outputEdges = []
        self.flatMatrix = list(it.chain(*matrix))

    def getStartValue(self):
        self.startValue = self.flatMatrix[id]

    def getValue(self):
        return self.sigmoid(self.startValue)

class NetworkNode(Node): # outputNodes
    temp = 0
    def getValue(self):
        for x in self.inputEdges:
            self.temp += self.sigmoid(self.inputEdges[x].getValue()) # ERROR returned Edge geen int
            print(self.temp)
        return self.temp
        

class Edge: # Edge
    def __init__(self):
        self.amplification = 1
        self.inputNode = None
        self.outputNode = None
        
    def getValue():
        print(self.inputNode.getValue())
        return self.inputNode.getValue() * self.amplification



inputNodes = []
outputNodes = []


def createNetwork(matrix):
    for x in range(2): # create output nodes
        outputNodes.append(NetworkNode())

    for x in range(9): # create input nodes
        inputNodes.append(BeginNode(x, matrix))
        for y in range(2):
            edge = Edge()
            inputNodes[x].inputEdges.append(edge)
            edge.inputNode = inputNodes[x]          # set edges input
            edge.outputNode = outputNodes[y]        # set edges output
            outputNodes[y].inputEdges.append(edge)  # set edge as input for output node


createNetwork(circle_1) # possibly easier to 'insert' list into the network into a function

outputNodes[0].getValue()

# print(list(it.chain(*cross_1)))

