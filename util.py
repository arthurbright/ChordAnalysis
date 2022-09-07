keyindex = ["a", "a#", "b", "c", "c#", "d", "d#", "e", "f", "f#", "g", "g#"]

#converts a key's index into the key  (0 = "a0", 1 = "a#0", etc)
def numtokey(n):
    key = keyindex[n % 12]
    octave = (n + 9)//12
    return key + str(octave)

#inverse of the above function. works even with .wav extension
def keytonum(key):
    if(key[1] == '#'):
        noteName = key[0:2]
        octave = int(key[2:3])
    else:
        noteName = key[0:1]
        octave = int(key[1:2])
    
    note = keyindex.index(noteName)
    if(note <= 2):
        return note + octave * 12
    else:
        return note + octave * 12 - 12
