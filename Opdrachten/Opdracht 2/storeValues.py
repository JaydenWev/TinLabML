import numpy as np
from csv import writer as wr

def storeEdgesInFile(fileName, values):
    np.savetxt(fileName, values, delimiter=",")

def storeNewEdgeElement(fileName, element):
    # Open file in append mode
    with open(fileName, 'a+', newline='') as write_obj:
        csv_writer = wr(write_obj) # Create a writer object from csv module
        csv_writer.writerow(element)
        write_obj.close()

def readEdgesFromFile():
    return np.genfromtxt('storedValues.csv', delimiter=',')

def readEdgeFromFile(x):
    return np.genfromtxt('storedValues.csv', delimiter=',')[x]
