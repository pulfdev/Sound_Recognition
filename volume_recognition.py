import pyaudio
import numpy as np
from pyAudioAnalysis import audioBasicIO
from pyAudioAnalysis import ShortTermFeatures
import wavio
from import_json import *

def record(duration=1, fs=4480):
        nsamples = duration * fs
        p = pyaudio.PyAudio()
        stream = p.open(
            format=pyaudio.paInt16, channels=1, rate=fs, input=True, frames_per_buffer=1024
        )
        buffer = stream.read(nsamples, exception_on_overflow=False)
        array = np.frombuffer(buffer, dtype="int16")
        stream.stop_stream()
        stream.close()
        p.terminate()
        return array


def start_and_save_recording():
    my_recording = record()
    wavio.write("recordings/pythonrecording.wav", my_recording, 44800, sampwidth=4)


def energies():
    [Fs, x] = audioBasicIO.read_audio_file("recordings/pythonrecording.wav")
    F, f_names = ShortTermFeatures.feature_extraction(x, Fs, 0.050 * Fs, 0.025 * Fs)
    energies = F[1, :]
    return energies








