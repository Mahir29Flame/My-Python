import os
import speech_recognition as sr
import pyaudio
import webbrowser
import pyttsx3
from news import get_news

recognizer = sr.Recognizer()
tts = pyttsx3.init()

def speak(output):
    print(f"Jarvis: {output}") # See it in the console too
    tts.say(output)
    tts.runAndWait()

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
    elif "facebook" in c.lower() or "fb" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "wikipedia" in c.lower():
        webbrowser.open("https://wikipedia.org")
    elif "open" in c.lower() and "news" in c.lower():
        webbrowser.open("https://news.google.com")
    elif "news" in c.lower():
        headlines = get_news()
        if headlines:
            speak("Here are the top headlines.")
            for headline in headlines:
                print(f"Reading: {headline}") # Debug print
                speak(headline)
        else:
            speak("I'm sorry, I couldn't fetch the news right now.")
    elif "reddit" in c.lower() or "red it" in c.lower():
        webbrowser.open("https://reddit.com")
    elif "linkedin" in c.lower() or "linked in" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "github" in c.lower():
        webbrowser.open("https://github.com")
    else : 
        speak("I didn't understand")

if __name__ == "__main__":
    speak("Initializing Jarvis...")
    r = sr.Recognizer() # Moved outside loop for better performance
    while True:
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=3, phrase_time_limit=2)
                word = r.recognize_whisper(audio, model="base")
                
                print("You said: " + word)
                if "jarvis" in word.lower():
                    speak("Ye?")
                    print("JARVIS Active...")
                    # Take the command immediately after 'Ye?'
                    command_audio = r.listen(source, timeout=3, phrase_time_limit=4)
                    command_text = r.recognize_whisper(command_audio, model="base")
                    print("Command: " + command_text)
                    proccesscommand(command_text)

        except sr.UnknownValueError:
            print("JARVIS could not understand audio")
        except Exception as e:
            print(f"JARVIS error; {e}")            