import muser as ms
import fileInteractor as fi
# ¿¿Optie voor afspeelsnelheid/BPM erbij zetten??

#where the music is stored
csvDir = 'Opdrachten/Opdracht 3/csv/'
songDir = 'Opdrachten/Opdracht 3/music/'

smallBlock = [
    [
        ('e', 8), ('f#', 8),
    ],
    [
        ('e', 4), ('f#', 4),
    ]
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


