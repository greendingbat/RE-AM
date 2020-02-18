class Chord:
    name = ""
    pattern = ()
    
    def __init__(self, name, pattern):
        self.name = name
        self.pattern = pattern


#Chords are represented as semitones from root note

Maj =       Chord("Maj", (0, 4, 7))
Min =       Chord("Min", (0, 3, 7))
Dom7 =      Chord("Dom7", (0, 4, 7, 10))
Maj7 =      Chord("Maj7", (0, 4, 7, 11))
Min7 =      Chord("Min7", (0, 3, 7, 10))
Maj6 =      Chord("Maj6", (0, 4, 7, 9))
Min6 =      Chord("Min6", (0, 3, 7, 9))
Dim =       Chord("Dim", (0, 3, 6))
Dim7 =      Chord("Dim7", (0, 3, 6, 9))
Dim7b5 =    Chord("7b5", (0, 3, 6, 10))   #Half diminished 7th
Aug =       Chord("Aug", (0, 4, 8))
Aug7Shrp5 = Chord("7#5", (0, 4, 8, 10))
Nine =      Chord("9th", (0, 4, 7, 10, 14))
Maj7Shrp9 = Chord("7#9", (0, 4, 7, 10, 15))
Maj9 =      Chord("Maj9", (0, 4, 7, 11, 14))
Add9 =      Chord("Add9", (0, 4, 7, 14))
Min9 =      Chord("Min9", (0, 3, 7, 10, 14))
MinAdd9 =   Chord("MinAdd9", (0, 3, 7, 14))
Eleven =    Chord("11", (0, 7, 10, 14, 17)) #Ommited third
Min11 =     Chord("Min11", (0, 3, 7, 10, 14, 17))

#Pwr =   (0, 7)

allChords = [Maj, Min, Dom7, Maj7, Min7, Maj6, Min6, Dim, Dim7, Dim7b5, Aug, Aug7Shrp5]

majorChords = [Maj, Min, Min, Maj, Maj, Min, Dim]
minorChords = [Min, Dim, Maj, Min, Min, Maj, Maj]
harmonicMinorChords = [Min, Dim, Aug, Min, Maj, Maj, Dim]
melodicMinorChords = [Min, Min, Aug, Maj, Maj, Dim, Dim]

