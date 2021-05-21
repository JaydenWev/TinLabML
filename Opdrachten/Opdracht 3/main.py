'''
'''
import muser as ms
import fileInteractor as fi

class Note:
    def __intit(self, note, length):
        self.note = note
        self.length = length
    '''
        (note, length) = ('f#', 8),
    '''

class Block: # Basic buildingBlock
    beat = 0
    notes = []
    def __inti__(self):
        pass

    '''
    Een block = ('e', 8), ('f#', 8),
        ('g*', 4), ('f#', 8), ('e', 8), ('d#*', 4), ('e', 8), ('f#', 8),
        ('b3*', 4), ('c#', 8), ('d#', 8), ('e*', 4), ('d', 8), ('c', 8),
        ('b3*', 4), ('a3', 8), ('g3', 8), ('f#3*', 4), ('g3', 8), ('a3', 8),
    1 tel per regel
    
    2d array met elke maat/note word opgeslagen (bach.py)
    '''

class Generation:
    genID = 0

class MusicGenerator:
    def __init__(self, generation):
        self.generation = generation
        musicGen = ms.Muser()
    '''
    Zet de /generation/blocken om naar een muziek file
    '''

