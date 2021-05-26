import csv

def writeToFile(path, data):
    f = open(path, 'w+')
    for t in data:
        line = '-'.join(str(x) for x in t)
        f.write(line + '\n')
    f.close()

def readFromFile(path):
    dataFile = open(path, 'r')
    dataReader = csv.reader(dataFile, delimiter = '-')
    data = [[],[]]
    for rowID, row in enumerate(dataReader):
        for value in row:
            newVal = eval(value)
            data[rowID].append(newVal)
    return data
