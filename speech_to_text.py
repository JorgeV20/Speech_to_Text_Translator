import speech_recognition as sr
from recording_audio import recording


recording('test.wav')

filename='test.wav'

r=sr.Recognizer()


# open the file
with sr.AudioFile(filename) as source:
    # listen for the data (load audio to memory)
    audio_data = r.record(source)
    # recognize (convert from speech to text) /it is using Google Speech Recognition
    text = r.recognize_google(audio_data)
    
    print(text)

