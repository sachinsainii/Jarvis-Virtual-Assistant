from speech_recognition.recognizers.google_cloud import recognize
import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import os
import requests
#from openai import OpenAI
#from gtts import gTTS
#import pygame


#pip install pocketsphinx
#pip install pygame
#pip install gTTS

# recognize = sr.Recognizer()
r = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "991a7cabd36644069ed23945599c3d84"

def speak(text):
    print("Jarvis: " , text)
    engine.say(text)
    engine.runAndWait()

"""def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3')

    pygame.mixer.init()
    pygame.mixer.music.load('temp.mp3')
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.music.unload()
    os.remove("temp.mp3")"""

"""def aiProcess(command):
    client = OpenAI(api_key="")
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system",
             "content": "you are a virtual assistant named jarvis skilled in general task like alexa and Google Cloud"},
            {"role": "user", "content": command}
        ]
    )
    return completion.choices[0].message.conten"""

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)

    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/everything?q=tesla&from=2025-05-11&sortBy=publishedAt&apiKey={newsapi}")
        if r.status_code == 200:
            data = r.json()

            articles = data.get["articles",[]]
            for article in articles:
                speak(article["title"])

    """else:
        output = aiprocess(c)
        speak(output)
        pass"""


if __name__ == "__main__":
    speak("Initializing Jarvis...")
    while True:
        r = sr.Recognizer()


        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening")
                audio = r.listen(source, timeout=10, phrase_time_limit=10)
            word = r.recognize_google(audio)
            print("You said: ", word)
            # if(word.lower() == "jarvis"):
            if "jarvis" in word.lower():
                speak("yesss sachin bro")
                with sr.Microphone() as source:
                    print("jarvis Active... Speak your command")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    print("Command: ", command)
                    processCommand(command)

        except Exception as e:
            print("Sorry, I could not understand your command. {0}".format(e))
