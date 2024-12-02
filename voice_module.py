import speech_recognition as sr
import sounddevice as sd
from gtts import gTTS
import os

def findAudioInputDevices():
    devices = sd.query_devices()
    #Per una questione di debug, stampo i dispositivi.
    print("Elenco dispositivi attaccati")
    for i, device in enumerate(devices):
        print(f"Index {i}: {device['name']}")
        print(f"  Input Channels: {device['max_input_channels']}")
        print(f"  Default Input Device: {device['max_input_channels']}\n")

    input_devices = [
        device for device in sd.query_devices()
        if device['max_input_channels'] > 0]

    print("\nDISPOSITIVI DI INPUT:")
    for device in input_devices:
        print(device['name'])

    # Dispositivo di default
    default_input = sd.default.device[1]

    print(f"\nDispositivo di Input Predefinito: {default_input}")


def recognize_speech():

    pass

def speak(text):
    pass