import muser as ms
import numpy as np
import musicBlocks as mbLib
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
    currentBlocks = [[],[]]
    blockIDs = []
    blockScores = [12, 9, 7, 11, 6, 12, 12, 8, 7, 14, 13, 10, 12, 8, 11, 10, 13, 10, 11, 9, 12, 10, 11, 8, 14]
    def readBaseBlocks(self): # Read the base/starter blocks
        pass

    def selectBlocksToUse(self): # Selects which block will be build
        pass # return func
    
    def updateBlockScore(self, adjustment): # Updates the score of currently used blocks
        pass
    
    def addBlockToSong (self, blockID):
        for x, row in enumerate(mbLib.blocks[blockID]):
            for y, column in enumerate(mbLib.blocks[blockID][x]):
                self.currentBlocks[x].append(mbLib.blocks[blockID][x][y])
        #print ("current after adding:",self.currentBlocks)


sc = SongCreater()
user = UserInputHandeler()
bc = BlockController()
muser = ms.Muser ()
print(mbLib.blocks[0][0])

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
    


arr = bc.blockScores
n = 4
ind = np.argpartition(arr, -n)[-n:]
print("index van hoogste : ", n, " ", ind)


bc.addBlockToSong(2) # Adds block to current block located in bc
bc.addBlockToSong(1)
bc.addBlockToSong(0)
sc.generateSong(bc.currentBlocks,"song1.wav")
print("currentBlocks:\n", bc.currentBlocks)

max_val = max(bc.blockScores)
index_max = bc.blockScores.index(max_val)

print('max val: ', max_val)
print(index_max)

