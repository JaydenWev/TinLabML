import csv

def writeToFile(path, data):
    f = open(path, 'w')
    for block in data:
        for t in block:
            line = '-'.join(str(x) for x in t)
            f.write(line + '\n')
    f.close()

def readFromFile(path):
    dataFile = open(path, 'r')
    dataReader = csv.reader(dataFile, delimiter = '-')
    data = []
    for row in dataReader:
        data.append(row)
    return data
