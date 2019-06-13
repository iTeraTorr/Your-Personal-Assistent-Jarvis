import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import sys
import requests
import bs4
import time,random
from pynput.keyboard import Key, Controller
keyboard=Controller()
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sirrr!")
    elif hour>=12 and hour<17:
        speak("Good Afternoon! Sirrr")
    else:
        speak("Good Evening!! Sirrr")

    speak("Please tell me how may I help you ? ")
def takeCommand():
    #it takes microphone input from user and returns string as output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold =600
        audio=r.listen(source)

    try:
        print("Recognizing...")
        query= r.recognize_google(audio, language='en-in')
        print(f"User said : {query}\n")

    except Exception as e:
        print(f"{e}\nSay that again please")
        return "None"
    return query
if __name__=="__main__":
    wishMe()
    while(True):
        query=takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query=query.replace('wikipedia','')
            try:
                results=wikipedia.summary(query,sentences=2)
            except Exception as e:
                speak("No internet connection found")
            speak('According to Wikipedia')
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'play music' in query:
            music_dir='E:\\Songs'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,random.choice(songs)))
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,Current time is {strTime}")
        elif 'open code' in query:
            codepath=("C:\\Users\\Ruchir\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code")
            os.startfile(codepath)
        elif 'quit' in query or 'exit' in query or 'leave' in query:
            break
        elif 'you do' in query:
            speak('I can do multiple things like telling time,opening google,youtube,stackoverflow,wikipedia, playing music and a lot more. What can I do for you sir ?')
        elif 'who are you' in query:
            speak('I am your very personal assistant Jarvis')
        elif 'made you' in query:
            speak('I was made in Udaipur by Ruchir Mehta also famously known as iterator')
        elif 'thank' in query:
            speak("you are always welcome sirrr")
        elif 'write' in query or 'type' in query:
            if 'write' in query:
                word='write'
            elif 'type' in query:
                word='type'
            write=query.replace(word,'')
            for char in write:
                keyboard.press(char)
                keyboard.release(char)
                time.sleep(0.12)
        elif 'setting' in query or 'settings' in query:
            speak('Opening settings')
            keyboard.press(Key.cmd)
            keyboard.press('i')
            keyboard.release(Key.cmd)
            keyboard.release('i')
        elif 'morning' in query or 'afternoon' in query or 'evening' in query:
            wishMe()
        elif 'close' in query:
            keyboard.press(Key.alt_l)
            keyboard.press(Key.f4)
            keyboard.release(Key.f4)
            keyboard.release(Key.alt_l)
        elif 'notepad' in query:
            speak("Opening Notepad")
            codepath=("C:\\Users\\Ruchir\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Notepad")
            os.startfile(codepath)
        elif 'minimise' in query:
            speak("Window Minimized")
            keyboard.press(Key.cmd)
            keyboard.press(Key.down)
            keyboard.release(Key.down)
            keyboard.press(Key.down)
            keyboard.release(Key.down)
            keyboard.release(Key.cmd)
        elif 'open' in query and 'window' in query:
            speak("Window Reopened")
            keyboard.press(Key.cmd)
            keyboard.press(Key.up)
            keyboard.release(Key.up)
            keyboard.press(Key.up)
            keyboard.release(Key.up)
            keyboard.release(Key.cmd)
        elif 'media player' in query:
            speak("Opening VLC Media Player")
            codepath=("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\VideoLAN\\VLC media player")
            os.startfile(codepath)
            
    speak('Thank You for using me Sirr')
