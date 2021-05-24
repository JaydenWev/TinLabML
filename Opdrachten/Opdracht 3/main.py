'''

'''
import muser as ms
import fileInteractor as fi

class Note:
    def __init__(self, note, length):
        self.note = note
        self.length = length

    def getValues(self):
        return [self.note, self.length]
    '''(note, length) = ('f#', 8),
    '''

class Block: # Basic buildingBlock
    notes = []
    def __init__(self, assignedNotes):
        self.notes = assignedNotes

    '''
    Een block = ('e', 8), ('f#', 8),
        ('g*', 4), ('f#', 8), ('e', 8), ('d#*', 4), ('e', 8), ('f#', 8),
        ('b3*', 4), ('c#', 8), ('d#', 8), ('e*', 4), ('d', 8), ('c', 8),
        ('b3*', 4), ('a3', 8), ('g3', 8), ('f#3*', 4), ('g3', 8), ('a3', 8),
    
    2d array met elke maat/note word opgeslagen (bach.py)
    '''

class Generation:
    genID = 0

class MusicGenerator:
    # Optie voor afspeelsnelheid/BPM
    def __init__(self, generation):
        self.generation = generation
        musicGen = ms.Muser()
    '''
    Zet de generation/blocken om naar een muziek file
    '''


#where the music is stored
pathToFile = 'Opdrachten/Opdracht 3/data.csv'
block = (
    (
        ('e', 8), ('f#', 8),
        ('g*', 4), ('f#', 8), ('e', 8), ('d#*', 4), ('e', 8), ('f#', 8),
        ('b3*', 4), ('c#', 8), ('d#', 8), ('e*', 4), ('d', 8), ('c', 8),
        ('b3*', 4), ('a3', 8), ('g3', 8), ('f#3*', 4), ('g3', 8), ('a3', 8)
    ),
    (
        ('e', 4), ('f#', 4),
    )
),

smallBlock = (
    (
        ('e', 8), ('f#', 8),
    ),
    (
        ('e', 4), ('f#', 4),
    )
),


fi.writeToFile(pathToFile, smallBlock)
data = fi.readFromFile(pathToFile)

print(data[0][0])
print('\n')
print(data)