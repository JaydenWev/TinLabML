import json

def writeToFile(path, data):
    with open(path, 'w') as outfile:
        json.dump(data, outfile)

def readFromFile(path):
    with open(path) as File:
        score = json.load(File)
        return score
