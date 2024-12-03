import speech_recognition as sr
import numpy as nmp
import sounddevice as sd
from dotenv import load_dotenv
from gtts import gTTS
import os

def findAudioInputDevices():
    devices = sd.query_devices()
    deviceName = "Microfono"

    #Per una questione di debug, stampo i dispositivi.
    print("Elenco dispositivi attaccati")
    for i, device in enumerate(devices):
       # if deviceName.lower() == device['name'].lower and device['max_input_channels']>0:
       #     sd.default.device(None, i)#la prima indica output, secondo input
        print(f"Index {i}: {device['name']}")
        print(f" Input Channels: {device['max_input_channels']}")
        print(f" Default Input Device: {device['max_input_channels']}\n")

    input_devices = [
        device for device in sd.query_devices()
        if device['max_input_channels'] > 0]

    print("\nDISPOSITIVI DI INPUT:")
    for device in input_devices:
        print(device['name'])

    # Dispositivo di default
    default_input = sd.default.device[1]

    print(f"\nDispositivo di Input Predefinito: {default_input}")
    #eventualmente settare il sample rate


def recognize_speech():
    load_dotenv()

    pass

def speak(text):
    pass