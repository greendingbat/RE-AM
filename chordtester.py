#import midiutil
import chords

noteSequence = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']


majorScale = [2, 2, 1, 2, 2, 2, 1]
minorScale = [2, 1, 2, 2, 1, 2, 2]

rootNote = input("Enter root note: ")
print()

majKey = []
minKey = []

# Generate major scale
pos = noteSequence.index(rootNote)
for i in majorScale:
    majKey.append(noteSequence[pos])
    pos = (pos + i) % len(noteSequence)

print("Notes in " + rootNote + "major scale:")
print(majKey)
print()

# Generate minor scale
pos = noteSequence.index(rootNote)
for i in minorScale:
    minKey.append(noteSequence[pos])
    pos = (pos + i) % len(noteSequence)

print("Notes in " + rootNote + "minor scale:")
print(minKey)
print()


# Print all key chords in major key
print("Chords in " + rootNote + " major key:")
for i in range(len(majKey)):
    pos = noteSequence.index(majKey[i])
    notes = ""
    chord = chords.majorChords[i]
    for j in chord.pattern:
        notes += noteSequence[(pos + j) % 12] + " "
    print(majKey[i] + chord.name + ":\t" + notes)
print()

# Print all key chords in minor key
print("Chords in " + rootNote + " minor key:")
for i in range(len(minKey)):
    pos = noteSequence.index(minKey[i])
    notes = ""
    chord = chords.minorChords[i]
    for j in chord.pattern:
        notes += noteSequence[(pos + j) % 12] + " "
    print(minKey[i] + chord.name + ":\t" + notes)
print()

# Print all chords rooted at rootNote
print("All chords rooted at " + rootNote)
pos = noteSequence.index(rootNote)
for i in range(len(chords.allChords)):
    notes = ""
    chord = chords.allChords[i]
    for j in chord.pattern:
        notes += noteSequence[(pos + j) % len(noteSequence)] + " "
    print(rootNote + chord.name + ":\t" + notes)
