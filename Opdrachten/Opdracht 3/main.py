''' Boyd Jayden Keanu

Prioritized requirements
    Seperate file with the music blocks.
    Each music block as a score
    User must be able to listen to all songs before grading

Main design choices
    All song should be created by one class/object
    Each created sequence of music block should be created in there own object
Test specification
    1.  After the grades are given it shoulld have effect on the scores
    Passed: The scores change accordingly yo the given grades
    Fail: The scores don't change
    2.  Create new set of 10 songs
    Passed: The new songs are created and the old files overwritten
    Fail: The new songs are created and saved with a copy indication in their name

'''
import muser as ms
import numpy as np
import musicBlocks as mbLib
import random
import FileInteractorJSON as fi
# ¿¿Optie voor afspeelsnelheid/BPM erbij zetten??

#where the music is stored
jsonDir = 'data/data.json'
songDir = 'music/'

class SongCreater:
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
        for counter in range(self.songBlockLength):
            indexNumber = availableIndex[random.randint(0,len(availableIndex)-1)] # Random number under availableIndex
            # print(indexNumber)
            self.addBlockToSong(indexNumber)
    
    def addBlockToSong (self, blockID):
        for rowIndex, row in enumerate(mbLib.blocks[blockID]):
            for columnIndex, column in enumerate(mbLib.blocks[blockID][rowIndex]):
                self.currentBlocks[rowIndex].append(mbLib.blocks[blockID][rowIndex][columnIndex])
        self.currentblockIDs.append(blockID)
        # print ("current after adding:",self.currentBlocks)
            
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

generationBlockIDs = []

# Run the code to generate the songs
def generateSong():
    for controllerID, blockController in enumerate(blockGeneration):
        blockController.readScores(jsonDir)
        blockController.selectBlocksToUse()
        
        generationBlockIDs.append(blockController.currentblockIDs)
        
        sc.generateSong(blockController.currentBlocks, 'song_'+str(controllerID)+'.wav')
    
generateSong()
user.changeScore(generationBlockIDs)
