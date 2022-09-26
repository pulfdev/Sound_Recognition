from vosk import Model, KaldiRecognizer
import pyaudio
from import_json import *

model = Model("vosk-model-small-en-us-0.15")
recogniser = KaldiRecognizer(model, 16000)

def recognise_words():
    
    cap = pyaudio.PyAudio()
    stream = cap.open(
        format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192
    )
    stream.start_stream()

    streaming = True

    while streaming:
        data = stream.read(4096)

        if recogniser.AcceptWaveform(data):
            said = recogniser.Result()
            x = said.partition(":")
            word = x[2].partition("\n") 
            word2 = word[0]
            word3 = word2.replace('"', "")             
            streaming = False
    stream.stop_stream()
    print(word3)
    return word3.strip()

def train_sounds(sound_name, number):
    while number !=0:
        print("say " + sound_name)
        word = recognise_words()
        user_made_sounds[word] = sound_name #TO DO: create user_made_sounds_dict
        number = number-1
    

def train_default_sounds(number):
    print("Do not worry if what you say does not match the sound exactly.")
    train_sounds("ay", number)
    train_sounds("ah", number)
    train_sounds("ee", number)
    save_user_changes()

def get_user_sounds(users_sounds = user_made_sounds): # TO DO: change print statements eventually 
    print("Say sounds to trigger a shortcut")
    sound_string = ""
    words_spoken = " "
    while words_spoken != [""]: 
        words_spoken = recognise_words().split(" ")
        for word in words_spoken:
            if word in users_sounds:
                sound = users_sounds[word]
                sound_string = sound_string + sound + " "
            else:
                print("this sound is not allocated")
    print(sound_string)
    return sound_string


def shortcut_exists(dictionary, sound):
    while True:
        try:
            shortcut_sound = list(dictionary.keys())[list(dictionary.values()).index(sound)]
            return shortcut_sound
        except ValueError:
            return "Does not exist"



def trigger_shortcut(sound_string, shortcut_dictionary): #TO DO: Change to json ones 
    stripped_sound_string = sound_string.strip() 
    if stripped_sound_string == '':
        return 0
    else:
        x = shortcut_exists(shortcut_dictionary, stripped_sound_string)
        if x == "Does not exist":
            print( stripped_sound_string + " is not a shortcut sound in this mode.")
            return ""
        else: 
            return x 


