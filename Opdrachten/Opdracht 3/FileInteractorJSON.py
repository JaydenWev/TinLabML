import json

def writeToFile(path, data):
    with open(path, 'w') as outfile:
        json.dump(data, outfile)

def readFromFile(path):
    with open(path) as File:
        score = json.load(File)
        print(score)

scores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

#writeToFile('data.json', scores)

readFromFile('data.json')