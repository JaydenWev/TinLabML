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

    def changeScore(self,melodiesPosition): # gets the user opinion 
        melodiesScore = fi.readFromFile(jsonDir)
        for iMelodie in range(len(melodiesPosition)):
             score = self.getUserInput(iMelodie)
             for block in melodiesPosition[iMelodie]:
                melodiesScore[block] += score 
                
        fi.writeToFile(jsonDir, melodiesScore)
  
             
    def getUserInput(self, iMelodie):
        while True :
            rate = int(input("What rate do you give melodie" + str(iMelodie) + ". choose: between 0-10\n"))
            if rate <= 10 and rate >= 0:
                return rate-5
            print('Answer needs to be between 0-10')
           
    def getRating(self):
        return self.ratingMelodies

class BlockController: # Decides which block are placed in  the song
    
    

    def __init__(self, length, id):
        self.songBlockLength = length
        self.readScores(jsonDir)
        self.id = id
        self.blockScores = []
        self.currentblockIDs = []    # ID of music blocks in currentBlocks
        self.baseBlocks = []
        self.currentBlocks = [[],[]] # Music block for current song

    def selectBlocksToUse(self): # Selects which block will be build
        availableIndex = self.getTopScores(10) # Get 10 highest scores
        # 8 keer herhaald worden
        for x in range(self.songBlockLength):
            indexNumber = random.randint(0,len(availableIndex)-1)
            # print(indexNumber)
            self.addBlockToSong(indexNumber)
    
    def addBlockToSong (self, blockID):
        for rowIndex, row in enumerate(mbLib.blocks[blockID]):
            for columnIndex, column in enumerate(mbLib.blocks[blockID][rowIndex]):
                self.currentBlocks[rowIndex].append(mbLib.blocks[blockID][rowIndex][columnIndex])
        self.currentblockIDs.append(blockID)
        # print ("current after adding:",self.currentBlocks)
    
    def checkIfEqual(self, oldSong):
        if oldSong == self.currentBlocks:
            return 1
        else:
            return -1
            
    def getTopScores(self, amount):
        indices = np.argpartition(self.blockScores, -amount)[-amount:]
        # print("index van hoogste : ", amount, " ", indices)
        return indices
    
    def readScores(self, path):
        self.blockScores = fi.readFromFile(path)
    
    def getCurrentBlockIDs(self):
        return (self.currentblockIDs)
    def printIDs(self):
        print('ControllerID: ',self.id, 'BlockIDs: ',self.currentblockIDs)
    def printScores(self):
        print(self.blockScores)


sc = SongCreater()
user = UserInputHandeler()
bc = BlockController(8, 99)
muser = ms.Muser ()
bc_1 = BlockController(8, 1)
bc_2 = BlockController(8, 2)
bc_3 = BlockController(8, 3)
bc_4 = BlockController(8, 4)
bc_5 = BlockController(8, 5)
bc_6 = BlockController(8, 6)

blockGeneration = []
blockGeneration.append(BlockController(8, 1))
blockGeneration.append(BlockController(8, 2))
blockGeneration.append(BlockController(8, 3))
blockGeneration.append(BlockController(8, 4))
blockGeneration.append(BlockController(8, 5))
blockGeneration.append(BlockController(8, 6))
blockGeneration.append(BlockController(8, 7))
blockGeneration.append(BlockController(8, 8))
blockGeneration.append(BlockController(8, 9))
blockGeneration.append(BlockController(8, 10))

def testUserInput():
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

# check how to update the scores
array = [   [1,2,3,4,5,6,7,8],
            [2,2,2,2,2,2,2,2],

        ]

for x in range(2):
    print(array[x])
    
    
print(user.changeScore(array))



# Create randomized song
# sc.generateSong(bc.currentBlocks, 'test.wav')
print('blockGeneration: '+str(len(blockGeneration)))
for controllerID, blockController in enumerate(blockGeneration):
    blockController.readScores(jsonDir)
    blockController.selectBlocksToUse()
    
    sc.generateSong(blockController.currentBlocks, 'song_'+str(controllerID)+'.wav')
    
