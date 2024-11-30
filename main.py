from ai_module import setup_openai, ask_openai
from voice_module import recognize_speech, speak, findAudioInputDevices
import vosk
import pvporcupine

#from image_module import capture_photo
#from movement_module import move_forward, stop
#from config import API_KEY

# Setup iniziale
#setup_openai(API_KEY)


def main():
    i = 0
    while (i<2):
        findAudioInputDevices(); i += 1


if __name__ == "__main__":
    main()
