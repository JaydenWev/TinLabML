# Jayden
import numpy as np
from csv import writer as wr

class fileInteractor:
    def storeInFile(self, fileName, values):
        np.savetxt(fileName, values, delimiter=",")

    def storeNewElement(self, fileName, element):
        # Open file in append mode
        with open(fileName, 'a+', newline='') as write_obj:
            csv_writer = wr(write_obj) # Create a writer object from csv module
            csv_writer.writerow(element)
            write_obj.close()

    def readFromFile(self, fileName):
        return np.genfromtxt(fileName, delimiter=',')

    def readFromFile(self, fileName):
        return np.genfromtxt(fileName, delimiter=',')
