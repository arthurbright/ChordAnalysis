from pydub import AudioSegment
import matplotlib.pyplot as plt
import numpy as np
import util
sound1 = AudioSegment.from_file("pianoSamples/c7.wav", format="wav")
sound2 = AudioSegment.from_file("pianoSamples/e2.wav", format="wav")

#re-index music files + trim them and convert to mono
#for i in range(88):
#    sound = AudioSegment.from_file("pianoSamples/" + str(util.numtokey(i)) + ".wav", format="wav")
#    newsound = sound.set_channels(1)
#    newsound = newsound[100:500]
#    newsound.export("pianomonoindexed/" + str(i) + ".mp3", format="mp3")

# Overlay sound2 over sound1 at position 0  (use louder instead of sound1 to use the louder version)
#overlay = sound1.overlay(sound2, position=0)



# simple export
#file_handle = overlay.export("outputcut.mp3", format="mp3")


#plan: 
#test out spectrogram and pyplot
#generate test samples (use set_channels(1) to turn stereo into mono)
#train model to identify all notes + base note
#make function to convert notes + base note into chord

#https://stackoverflow.com/questions/43877971/librosa-pitch-tracking-stft: 
#USE DFT spaced at desired pitches ONLY; make much easier