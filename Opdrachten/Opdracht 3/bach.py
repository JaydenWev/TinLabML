import muser as ms

bach = [
    [
        ('a', 8), ('a', 8),
    ],
    [
        ('b', 8), ('b', 8),

    ]
]

bach2 = [
    [
        ('c', 8), ('c', 8),
    ],
    [
        ('e', 8), ('e', 8),

    ]
]






###zit in een lijst van blocken
blockFromList = [[
    ('f', 8), ('f', 8),
    ],[
    ('g', 8), ('g', 8),
    ]]

def addBlockToSong (returnedBlock):
    #vertical, horizontal
    print (returnedBlock[0][1])
    print (len(returnedBlock[0]))   #lengte boven
    print (len(returnedBlock[1]))   #lengte onder
    for x in range(len(returnedBlock[0])):
        for y in range(len(returnedBlock[x])):
            print (x,y)
            bach[x].append(returnedBlock[x][y])

    print(bach)
#bach[0].append(('g1', 1))
#bach[0].append(('g1', 1))
#bach[1].append(('g1', 1))
#bach[1].append(('g1', 1))

addBlockToSong(blockFromList)

muser = ms.Muser ()
muser.generate (bach,"music\song.wav")
