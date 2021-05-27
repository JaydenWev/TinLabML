import muser as ms
import fileInteractor as fi
# ¿¿Optie voor afspeelsnelheid/BPM erbij zetten??

#where the music is stored
csvDir = 'Opdrachten/Opdracht 3/csv/'
songDir = 'Opdrachten/Opdracht 3/music/'

firstBlock = [
    [
        ('f', 4),
        ('g', 4),
        ('f', 4),
        ('g', 4), 
    ],
    [
        ('a', 16),('b', 16),('c', 16),('d', 16),
        ('a', 16),('b', 16),('c', 16),('d', 16),
        ('a', 16),('b', 16),('c', 16),('d', 16),
        ('a', 16),('b', 16),('c', 16),('d', 16),
    ],
]
secondBlock = [
    [
        ('e', 4),
        ('d', 4),
        ('b', 4),
        ('a', 4),  
    ],
    [
        ('c2', 16),('c2', 16),('c2', 16),('c2', 16),
        ('c2', 12),('c2', 12),('c2', 12),
        ('c2', 8),('c2', 8),
        ('c2', 4),
    ],
]
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
    baseBlocks = []
    currentBlocks = [[],[]]
    def setCurrentBlock(self, blockToSet):
        self.currentBlocks = blockToSet
        #print("current: ",self.currentBlocks)
    def readBaseBlocks(self): # Read the base/starter blocks
        pass

    def selectBlocksToUse(self): # Selects which block will be build
        pass # return func
    
    def updateBlockScore(self, adjustment): # Updates the score of currently used blocks
        pass
    
    def addBlockToSong (self, returnedBlock):
        for x, row in enumerate(returnedBlock):
            for y, column in enumerate(returnedBlock[x]):
                self.currentBlocks[x].append(returnedBlock[x][y])
        #print ("current after adding:",self.currentBlocks)


sc = SongCreater()
user = UserInputHandeler()
bc = BlockController()
muser = ms.Muser ()


bc.setCurrentBlock(firstBlock) #overwrites current block with parameter
bc.addBlockToSong(secondBlock) #adds block to current block located in bc
sc.generateSong(bc.currentBlocks,"song1.wav")




print(user.getUserInput())

