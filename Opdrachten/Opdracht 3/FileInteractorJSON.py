import json

def writeToFile(path, data):
    with open('data.json', 'w') as outfile:
        json.dump(data, outfile)

def readFromFile(path, variable):
    with open('data.json') as File:
        bach2 = json.load(File)
        for p in bach2:
            return p[variable]
