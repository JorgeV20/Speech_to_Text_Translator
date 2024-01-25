# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 18:49:32 2023

@author: Jorge
"""
import pyaudio
import wave
import numpy as np


def recording(wav_output_filename):
    form_1 = pyaudio.paInt16
    chans = 1 # 1 channel
    samp_rate = 44100
    chunk = 1024
    record_secs = 5
    #dev_index = 2 
    wav_output_filename = wav_output_filename # name of .wav file
    
    audio = pyaudio.PyAudio() # create pyaudio instantiation
    
    # create pyaudio stream
    stream = audio.open(format = form_1,rate = samp_rate,channels = chans, input = True,frames_per_buffer=chunk)
    print("recording")
    frames = []
    
    # loop through stream and append audio chunks to frame array
    for ii in range(0,int((samp_rate/chunk)*record_secs)):
        data = stream.read(chunk)
        frames.append(data)
    
    print("finished recording")
    
    # stop the stream, close it, and terminate the pyaudio instantiation
    stream.stop_stream()
    stream.close()
    audio.terminate()
    
    # save the audio frames as .wav file
    wavefile = wave.open(wav_output_filename,'wb')
    wavefile.setnchannels(chans)
    wavefile.setsampwidth(audio.get_sample_size(form_1))
    wavefile.setframerate(samp_rate)
    wavefile.writeframes(b''.join(frames))
    wavefile.close()
    
    return True
    
#recording('prueba.wav')