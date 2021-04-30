import math as mt
vector = [689,68] # test vector
def normalize(vector):
    factor = mt.sqrt(mt.pow(vector[0],2) + mt.pow(vector[1],2)) #sqaures the two values and take the sqrt from items
    vector[0] /= factor # take the quotient to normalize the vector
    vector[1] /= factor
    return vector # return the normalized vector
print(normalize(vector))


def sigmoid(x):
        return  1 / (1 + mt.exp(-x))
print(sigmoid(1))