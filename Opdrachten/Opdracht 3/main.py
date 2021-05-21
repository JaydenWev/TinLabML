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

note_A4 = Note('a', 4)
note_A8 = Note('a', 8)
note_B4 = Note('b', 4)
note_B8 = Note('b', 8)
note_C4 = Note('c', 4)
note_C8 = Note('c', 8)
note_D4 = Note('d', 4)
note_D8 = Note('d', 8)
note_E4 = Note('e', 4)
note_E8 = Note('e', 8)

aNotes = [note_A4, note_A8]

block_1 = Block(aNotes)

print(block_1.notes[0].getValues())
print(block_1.notes[1].getValues())