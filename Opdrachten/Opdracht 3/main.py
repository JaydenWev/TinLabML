import muser as ms
import numpy as np
import musicBlocks as mbLib
import random
# ¿¿Optie voor afspeelsnelheid/BPM erbij zetten??

#where the music is stored
csvDir = 'Opdrachten/Opdracht 3/csv/'
songDir = 'Opdrachten/Opdracht 3/music/'


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

    def generateSong(self, blocks,name): # Creates the music
        muser.generate (blocks,"music\\"+ name)
        pass

class UserInputHandeler:
    score = 0
    ratingMelodies = []
    def getUserInput(self): # gets the user opinion 
        self.ratingMelodies = []
        for iMelodie in range(10):
            self.ratingMelodies.append(self.ratingMelodieNumber(iMelodie))
        return self.ratingMelodies
             
    def ratingMelodieNumber(self, iMelodie):
        while True :
            rate = input("What rate do you give melodie" + str(iMelodie) + ". choose: good/bad\n")
            if rate == "good":
                return 1
            if rate == "bad" :
                return -1
            print('Answer needs to be "good" or "bad"')

        

    def getScore(self):
        return self.score

class BlockController:
    songBlockLength = 0
    baseBlocks = []
    currentBlocks = [[],[]] # Music block for current song
    currentblockIDs = []    # ID of music blocks in currentBlocks
    blockScores = [12, 9, 7, 11, 6, 12, 12, 8, 7, 14, 13, 10, 12, 8, 11, 10, 13, 10, 11, 9, 12, 10, 11, 8, 14]
    
    def __init__(self, songLength):
        self.songBlockLength = songLength

    def selectBlocksToUse(self): # Selects which block will be build
        availableIndex = self.getTopScores(10)
        # 8 keer herhaald worden
        for x in range(self.songBlockLength):
            indexNumber = random.randint(0,len(availableIndex)-1)
            # print(indexNumber)
            self.addBlockToSong(indexNumber)
        pass # return func
    
    def updateBlockScore(self, adjustment): # Updates the score of currently used blocks
        pass
    
    def addBlockToSong (self, blockID):
        for x, row in enumerate(mbLib.blocks[blockID]):
            for y, column in enumerate(mbLib.blocks[blockID][x]):
                self.currentBlocks[x].append(mbLib.blocks[blockID][x][y])
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


sc = SongCreater()
user = UserInputHandeler()
bc = BlockController(8) # Pass through amount of blocks in a song
muser = ms.Muser ()

bc.selectBlocksToUse()
print(bc.currentBlocks)