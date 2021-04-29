import math as mt
vector = [689,68]
def setDistanceToOne(vector):
    factor = mt.sqrt(mt.pow(vector[0],2) + mt.pow(vector[1],2))
    vector[0] /= factor
    vector[1] /= factor
    return vector
print(setDistanceToOne(vector))