import muser as ms
import numpy as np
import musicBlocks as mbLib
import random
import FileInteractorJSON as fi
# ¿¿Optie voor afspeelsnelheid/BPM erbij zetten??

#where the music is stored
jsonDir = 'data/data.json'
songDir = 'music/'


'''
# Save to file
csvName = 'data.csv'
fi.writeToFile(csvDir+csvName, smallBlock)
# read from file
data = fi.readFromFile(csvDir+csvName)

muser = ms.Muser()
# Save music file to location
songName = 'song.wav'
muser.generate(data, songDir+songName)
'''


class SongCreater:    
    def assembleSongList(self): # 8 blokken verzamelen in een lijst 
        pass

    def generateSong(self, blocks, name): # Creates the music
        path = songDir+name
        muser.generate (blocks, path)
        print('File saved to: ', path)

class UserInputHandeler:
    ratingMelodies = []
    def getUserInput(self,amountOfMelodies): # gets the user opinion 
        self.ratingMelodies = []
        for iMelodie in range(amountOfMelodies):
            self.ratingMelodies.append(self.ratingMelodieNumber(iMelodie))
        return self.ratingMelodies
             
    def ratingMelodieNumber(self, iMelodie):
        while True :
            rate = int(input("What rate do you give melodie" + str(iMelodie) + ". choose: between 0-10\n"))
            if rate <= 10 and rate >= 0:
                return rate-5
            print('Answer needs to be between 0-10')
    
    def changeScore(self, melodies):
        score = self.getUserInput(len(melodies))
        newScore = []
        for Imelodie, melodie in enumerate(melodies):
            melodie = [x + score[Imelodie] for x in melodie]
            newScore.append(melodie)
        
        return newScore
            
        
   
    def getRating(self):
        return self.ratingMelodies

class BlockController:
    baseBlocks = []
    currentBlocks = [[],[]] # Music block for current song
    currentblockIDs = []    # ID of music blocks in currentBlocks
    blockScores = []

    def __init__(self, length):
        self.songBlockLength = length
        self.readScores(jsonDir)

    def selectBlocksToUse(self): # Selects which block will be build
        availableIndex = self.getTopScores(10)
        # 8 keer herhaald worden
        for x in range(self.songBlockLength):
            indexNumber = random.randint(0,len(availableIndex)-1)
            # print(indexNumber)
            self.addBlockToSong(indexNumber)
    
    def updateBlockScore(self, adjustment): # Updates the score of currently used blocks
        pass
    
    def addBlockToSong (self, blockID):
        for rowIndex, row in enumerate(mbLib.blocks[blockID]):
            for columnIndex, column in enumerate(mbLib.blocks[blockID][rowIndex]):
                self.currentBlocks[rowIndex].append(mbLib.blocks[blockID][rowIndex][columnIndex])
        #print ("current after adding:",self.currentBlocks)
    
    def checkIfEqual(self, oldSong):
        if oldSong == self.currentBlocks:
            return 1
        else:
            return -1
            
    def getTopScores(self, amount):
        print ('\nmax Values')
        indices = np.argpartition(self.blockScores, -amount)[-amount:]
        # print("index van hoogste : ", amount, " ", indices)
        return indices
    
    def readScores(self, path):
        self.blockScores = fi.readFromFile(path)


sc = SongCreater()
user = UserInputHandeler()
bc = BlockController(8)
muser = ms.Muser ()

# check how to update the scores
array = [   [1,2,3,4,5,6,7,8],
            [8,7,6,5,4,3,2,1],
            [0,1,2,3,4,5,6,7],
            [7,6,5,4,3,2,1,0],
            [5,5,5,5,5,5,5,5],
            [4,4,4,4,4,4,4,4],
            [2,2,2,3,3,3,4,4],
            [0,0,0,1,1,1,2,2],
            [1,1,3,3,5,5,7,7],
            [0,0,0,0,0,0,0,0]  
        ]

for x in range(10):
    print(array[x])
    
newArray = user.changeScore(array)

for x in range(10):
    print(newArray[x])

# Create randomized song
bc.selectBlocksToUse()
sc.generateSong(bc.currentBlocks, 'test.wav')
