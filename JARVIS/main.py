import os
import speech_recognition as sr
import pyaudio
import webbrowser
import pyttsx3

recognizer = sr.Recognizer()
tts = pyttsx3.init()

def speak(output):
    tts.say(output)
    tts.runAndWait()

if __name__ == "__main__":
    speak("Initializing Jarvis...")
    while True:
        # Listening for the wake word 'Jarvis':
        # obtain audio from the microphone
        r = sr.Recognizer()

        # recognize speech using Sphinx
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            command = r.recognize_google(audio)
            print("You said: " + command)
            if command.lower() == "jarvis":
                speak("Ye?")
                with sr.Microphone() as source:
                    print("JARVIS Active...")
                    audio = r.listen(source, timeout=2, phrase_time_limit=1)

        except sr.UnknownValueError:
            print("JARVIS could not understand audio")
        except Exception as e:
            print(f"JARVIS error; {e}")
            