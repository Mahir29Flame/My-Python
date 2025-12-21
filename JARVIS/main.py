import os
import speech_recognition as sr
import pyaudio
import webbrowser
import pyttsx3

recognizer = sr.Recognizer()
tts = pyttsx3.init()
def proccesscommand(c):
    
    if "google" in c.lower() :
        webbrowser.open("https://google.com")
    elif "bing" in c.lower()  :
        webbrowser.open("https://bing.com")
    elif "gemini" in c.lower()  :
        webbrowser.open("https://gemini.com")
    elif "todo" in c.lower() or "tasks" in c.lower() :
        webbrowser.open("https://tasks.google.com")
    elif "calendar" in c.lower()   :
        webbrowser.open("https://calendar.google.com")
    elif "chatgpt" in c.lower()  :
        webbrowser.open("https://chatgpt.com")    
    elif "ai studio" in c.lower()  :
        webbrowser.open("https://aisudio.google.com")    
    elif "youtube" in c.lower() or "yt" in c.lower()  :
        webbrowser.open("https://youtube.com")
    elif "fb" or "facebook" in c.lower()  :
        webbrowser.open("https://facebook.com")
    elif "reddit" or "red it" in c.lower()  :
        webbrowser.open("https://reddit.com")
    elif "wikipedia" in c.lower()  :
        webbrowser.open("https://wikipedia.org")
    elif "linkedin" or "linked in" in c.lower()  :
        webbrowser.open("https://linkedin.com")
    elif "github" in c.lower()  :
        webbrowser.open("https://github.com")
    else : 
        speak("I didn't understand")



def speak(output):
    tts.say(output)
    tts.runAndWait()

if __name__ == "__main__":
    speak("Initializing Jarvis...")
    while True:
        # Listening for the wake word 'Jarvis':
        # obtain audio from the microphone
        r = sr.Recognizer()

        # recognize speech using _____
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_whisper(audio,model="tiny")
            print("You said: " + word)
            if word.lower() == "jarvis":
                speak("Ye?")
                with sr.Microphone() as source:
                    print("JARVIS Active...")
                    command = r.listen(source, timeout=2, phrase_time_limit=1)
                    proccesscommand(command)

        except sr.UnknownValueError:
            print("JARVIS could not understand audio")
        except Exception as e:
            print(f"JARVIS error; {e}")
            