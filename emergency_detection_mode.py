from import_json import *
import os 
from twilio.rest import Client
import pyaudio
from pyAudioAnalysis import audioBasicIO
from pyAudioAnalysis import ShortTermFeatures
import math
import struct
import wave
import time
import os
from import_json import *
from vowel_recognition import *


Threshold = emergency_detection_dict["Threshold"]

SHORT_NORMALIZE = 1.0 / 32768.0
chunk = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
swidth = 2

TIMEOUT_LENGTH = 1
FULL_TIMEOUT_LENGTH = 4

f_name_directory = r"./recordings"


class Recorder:
    @staticmethod
    def rms(frame):
        count = len(frame) / swidth
        format = "%dh" % (count)
        shorts = struct.unpack(format, frame)

        sum_squares = 0.0
        for sample in shorts:
            n = sample * SHORT_NORMALIZE
            sum_squares += n * n
        rms = math.pow(sum_squares / count, 0.5)

        return rms * 1000

    def __init__(self):
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(
            format=FORMAT,
            channels=CHANNELS,
            rate=RATE,
            input=True,
            output=True,
            frames_per_buffer=chunk,
        )

    def record(self):
        print("Noise detected, recording beginning")
        rec = []
        current = time.time()
        end = time.time() + TIMEOUT_LENGTH

        while current <= end:

            data = self.stream.read(chunk)
            if self.rms(data) >= Threshold:
                end = time.time() + TIMEOUT_LENGTH

            current = time.time()
            rec.append(data)
        self.write(b"".join(rec))

    def write(self, recording):
        n_files = len(os.listdir(f_name_directory))

        filename = os.path.join(f_name_directory, "{}.wav".format(n_files))

        wf = wave.open(filename, "wb")
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(self.p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(recording)
        wf.close()
        print("Written to file: {}".format(filename))
        print("Returning to listening")

    def listen(self):
        print("Listening beginning")
        no_emergency = True
        while no_emergency:
            input = self.stream.read(chunk)
            rms_val = self.rms(input)
            if rms_val > Threshold:
                self.record()
                morse_string = determine_morse_string("recordings/0.wav", 0.04)
                no_emergency = is_emergency(morse_string)

                
                



def determine_morse_string(recordings, threshold):

    x_array = []
    y_array = []
    feature_count = 0
    feature_size_array = []

    [Fs, x] = audioBasicIO.read_audio_file(recordings)
    F, f_names = ShortTermFeatures.feature_extraction(x, Fs, 0.050 * Fs, 0.025 * Fs)

    energies = F[1, :]

    i = 0
    while i < len(energies):
        size_of_feature = 0
        if energies[i - 1] > threshold:
            x_array.append(i - 1)
            y_array.append(energies[i - 1])
            feature_count = feature_count + 1
            while energies[i - 5] > threshold:
                if (i - 2) < len(energies):
                    size_of_feature = size_of_feature + 1
                    i = i + 1
                else:
                    break
        if size_of_feature != 0:
            feature_size_array.append(size_of_feature)
        i = i + 1

    morse_string = ""

    for size in feature_size_array:
        if size < 15:
            morse_string = morse_string + "s"
        else:
            morse_string = morse_string + "l"
    return morse_string


def is_emergency(morse_string):
    if morse_string == emergency_detection_dict["Emergency_string"]:
        print(morse_string)
        send_message(emergency_detection_dict["name"] + " is having an emergency. Please send help.")
        print("Message has been sent to " + emergency_detection_dict["ICE_Name"] + ". Help will be with you soon.")
        os.remove("recordings/0.wav")
        return False
    else:
        print(morse_string)
        os.remove("recordings/0.wav")
        return True

def send_message(message_to_send):
    TWILIO_ACCOUNT_SID = emergency_detection_dict["TWILIO_ACCOUNT_SID"]
    TWILIO_AUTH_TOKEN = emergency_detection_dict["TWILIO_AUTH_TOKEN"]

    account_sid = TWILIO_ACCOUNT_SID
    auth_token = TWILIO_AUTH_TOKEN
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
            body= message_to_send,
            from_= emergency_detection_dict["Twilio_phone_number"],
            to= emergency_detection_dict["ICE_phone_number"]
        )

def emergency_detection_mode():
    a = Recorder()
    a.listen()

def set_emergency_info():
    print("Please set your emergency information.")
    print("Do you have a Twill.io account and someone who is able to type for you?")
    print("Say " + settings_dict["a"] + " for yes")
    print("Say " + settings_dict["b"] + " for no")
    sound_string = get_user_sounds(user_made_sounds) 
    print(sound_string)
    if sound_string != "":
        y = trigger_shortcut(sound_string, settings_dict)
        if y == "a":
            a = input("Enter the name of the person who may be in an emergency:")
            emergency_detection_dict["name"] = a 
            b = input("Enter emergency contact's name:")
            emergency_detection_dict["ICE_Name"] = b
            c = input("Enter emergency contact's phone number with area code (e.g. +4407123456789):")
            c.strip()
            if c[0]!= "+":
                c = "+" + c
            emergency_detection_dict["ICE_phone_number"] = c
            d = input("Enter Twilio phone number (from the website):")
            d.strip()
            if d[0]!= "+":
                d = "+" + d
            emergency_detection_dict["Twilio_phone_number"] = d
            e = input("Enter TWILIO_ACCOUNT_SID (from the website):")
            emergency_detection_dict["TWILIO_ACCOUNT_SIDr"] = e
            f = input("Enter TWILIO_AUTH_TOKEN (from the website):")
            emergency_detection_dict["TWILIO_AUTH_TOKEN"] = f
            print("Thank you for that information.")
            loop = True
            while loop:
                for i in emergency_detection_dict:
                    print(i + ": " + str(emergency_detection_dict[i]))
                print("Is this all correct? Please check carefully as if there is any wrong information the text may not be sent in the emergency.")
                x = input("y/n? :")
                if x == 'y':
                    emergency_detection_dict["emergency_info_up_to_date"] = "True"
                    save_user_changes(dictionaries = dictionaries)
                    loop = False
                if x == "n": 
                    print("Please try again.")
                    set_emergency_info()
                    loop = False
                else:
                    print("Input not recognised. Please try again.")
