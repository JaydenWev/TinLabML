'''
Prioritized requirements
    Input is een 2d matrix

Main design choices


Test specification


'''
import math as mt

class Node:
    def __init__(self):
        self.inputEdges = []
        self.outputEdges = []

    def sigmoid(self, x):
        return  1 / (1 + mt.exp(-x))



class Edge:
    def __init__(self):
        self.amplification = 1
        self.inputNode = None
        self.outputNode = None


'''
nodes maken met koppeling naar elkaar

'''
cross_1 = [[0, 1, 0],
            [1, 1, 1],
            [0, 1, 0]]

cross_2 = [[1, 0, 1],
            [0, 1, 0],
            [1, 0, 1]]

circle_1 = [[1, 1, 1],
            [1, 0, 1],
            [1, 1, 1]]

circle_2 = [[0, 1, 0],
            [1, 0, 1],
            [0, 1, 0]]


OutputNodes = []
for x in range(2):
    OutputNodes.append(Node())

InputNodes = []
InputEdges = []
OutputEdges = []

for x in range(9):
    InputNodes.append(Node())
    for y in range(2):
        edge = Edge()
        InputNodes[x].inputEdges.append(edge)
        edge.inputNode = InputNodes[x]          # set edges input
        edge.outputNode = OutputNodes[y]        # set edges output

'''
1. inputNodes pakken een waarde van de matric en gooien die door de sigmoid()
2. waarde gaat door edge en wordt geamplified
3. in netwerkNode gaat de waarde door de sigmoid

de netwerkNodes die pakken de waarde van de inputNodes
    in de edges worden de waardes gemultiplied met de amplification

   Return value is een recusieve functie
   Nodes overerven
'''
