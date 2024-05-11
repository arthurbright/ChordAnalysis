from pydub import AudioSegment
import matplotlib.pyplot as plt
import numpy as np
import util
import math
import array

sound1 = AudioSegment.from_file("pianomonoindexed/40.mp3", format="mp3")
sound2 = AudioSegment.from_file("pianoSamples/g6.wav", format="wav")

#re-index music files + trim them and convert to mono
#for i in range(88):
#    sound = AudioSegment.from_file("pianoSamples/" + str(util.numtokey(i)) + ".wav", format="wav")
#    newsound = sound.set_channels(1)
#    newsound = newsound[100:500]
#    newsound.export("pianomonoindexed/" + str(i) + ".mp3", format="mp3")



# Overlay sound2 over sound1 at position 0  (use louder instead of sound1 to use the louder version)
#overlay = sound1.overlay(sound2, position=0)



# simple export
# sound1 += 5
sound1 = sound1.set_channels(1)
arr = sound1.get_array_of_samples()
noise = np.int_(np.round(np.random.normal(scale=100, size=len(arr))))
print(noise)
arr += noise

new_arr = array.array(sound1.array_type, arr)
newsound = sound1._spawn(new_arr)
file_handle = newsound.export("tl.mp3", format="mp3")


#plan: 
#test out spectrogram and pyplot
#generate test samples (use set_channels(1) to turn stereo into mono)
#train model to identify all notes + base note
#make function to convert notes + base note into chord

#https://stackoverflow.com/questions/43877971/librosa-pitch-tracking-stft: 
#USE DFT spaced at desired pitches ONLY; make much easier

#https://stackoverflow.com/questions/48097164/limiting-scipy-signal-spectrogram-to-calculate-only-specific-frequencies
#https://en.wikipedia.org/wiki/Piano_key_frequencies
#https://wiki.python.org/moin/UsingPickle
spec, freqs, times, dot = plt.specgram(newsound.set_channels(1).get_array_of_samples(), Fs=sound1.frame_rate, NFFT=8192, window=plt.mlab.window_none)
maxx = 0
ind = -1
count = 0
for arr in spec:
    count += 1
    if(arr[0] > maxx):
        maxx = arr[0]
        ind = count
print(maxx, ind)
plt.show()