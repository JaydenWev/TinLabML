import muser as ms
import fileInteractor as fi
# ¿¿Optie voor afspeelsnelheid/BPM erbij zetten??

#where the music is stored
pathToCsv = 'Opdrachten/Opdracht 3/csv/data.csv'
pathToMusic = 'Opdrachten/Opdracht 3/music/song.wav'

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