import muser as ms
import fileInteractor as fi
# ¿¿Optie voor afspeelsnelheid/BPM erbij zetten??

#where the music is stored
csvDir = 'Opdrachten/Opdracht 3/csv/'
songDir = 'Opdrachten/Opdracht 3/music/'

firstBlock = [
    [
        ('e', 8), ('f#', 8),
    ],
    [
        ('e', 4), ('f#', 4),
    ],
]
secondBlock = [
    [
        ('c', 8), ('b', 8),
    ],
    [
        ('e', 4), ('d', 4),
    ],
]

# Save to file
csvName = 'data.csv'
fi.writeToFile(csvDir+csvName, smallBlock)
# read from file
data = fi.readFromFile(csvDir+csvName)

muser = ms.Muser()
# Save music file to location
songName = 'song.wav'
muser.generate(data, songDir+songName)


class SongCreater:    
    def assembleSongList(self): # 8 blokken verzamelen in een lijst 
        pass

    def createSong(self, blocks): # Creates the music
        pass

class UserInputHandeler:
    score = 0

    def getUserInput(self):
        pass

    def getScore(self):
        return self.score

class BlockController:
    baseBlocks = []
    currentBlocks = []
    
    def readBaseBlocks(self): # Read the base/starter blocks
        pass

    def selectBlocksToUse(self): # Selects which block will be build
        pass # return func
    
    def updateBlockScore(self, adjustment): # Updates the score of currently used blocks
        pass




sc = SongCreater()
user = UserInputHandeler()

