import muser as ms
import fileInteractor as fi
# ¿¿Optie voor afspeelsnelheid/BPM erbij zetten??

#where the music is stored
csvDir = 'Opdrachten/Opdracht 3/csv/'
songDir = 'Opdrachten/Opdracht 3/music/'

smallBlock = (
    (
        ('e', 8), ('f#', 8),
    ),
    (
        ('e', 4), ('f#', 4),
    )
)

csvName = 'data.csv'
fi.writeToFile(csvDir+csvName, smallBlock)
# data = fi.readFromFile(csvDir)

muser = ms.Muser()
songName = 'song.wav'
muser.generate(smallBlock, songDir+songName)
