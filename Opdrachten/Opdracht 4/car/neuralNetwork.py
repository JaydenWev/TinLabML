import math as mt
import numpy as np
import itertools as it
import random

class Node: # Base node
    def __init__(self):
        self.inputEdges = []
        self.outputEdges = []
        self.value = 0

    def sigmoid(self, x):
        return  1 / (1 + mt.exp(-x))

class BeginNode(Node): # InputNodes
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
    def __init__(self, trainingSets):
        self.trainingSets = trainingSets
        self.inputNodes = []
        self.outputNodes = []
        self.nodesInOutputLayer = 2
        
    
    def createNetwork(self):
        for iOutput in range(self.nodesInOutputLayer): # Create output nodes
            self.outputNodes.append(NetworkNode())
            
        for iInput in range(len(self.trainingSets[0])): # Create input nodes
            self.inputNodes.append(BeginNode())
            for iOutput in range(self.nodesInOutputLayer):
                edge = Edge()
                self.inputNodes[iInput].outputEdges.append(edge)
                edge.inputNode = self.inputNodes[iInput]          # Set edges input
                edge.outputNode = self.outputNodes[iOutput]        # Set edges output
                self.outputNodes[iOutput].inputEdges.append(edge)  # Set edge as input for output node