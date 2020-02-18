import midiutil
import chords


majorScale = [2, 2, 1, 2, 2, 2, 1];
noteSequence = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']

rootNote = input("Enter root note: ")

pos = noteSequence.index(rootNote)
key = []

for i in majorScale:
    #print(noteSequence[pos])
    key.append(noteSequence[pos])
    pos = (pos + i) % len(noteSequence)

print()
print("Notes in " + rootNote + "major scale:")
print(key)
print()

pos = noteSequence.index(rootNote)
for i in range(len(chords.allChords)):
    notes = ""
    chord = chords.allChords[i]
    for j in chord:
        notes += noteSequence[(pos + j) % len(noteSequence)] + " "
    print(rootNote + chords.chordNames[i] + ": " + notes)
