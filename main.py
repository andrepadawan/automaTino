from ai_module import setup_openai, ask_openai
import os
from voice_module import recognize_speech, speak, findAudioInputDevices
from dotenv import load_dotenv
import vosk
import pvporcupine
from deviceSelection import findAudioInputDevices

#from image_module import capture_photo
#from movement_module import move_forward, stop
#from config import API_KEY

# Setup iniziale
#setup_openai(API_KEY)


def main():
    #test file .env
    #print(f"Sesso è samba = {os.getenv('Sesso_e_samba')}")
    findAudioInputDevices()


if __name__ == "__main__":
    main()
