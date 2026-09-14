import speech_recognition as sr;
import webbrowser;
import pyttsx3;
import MusicLibrary;
import requests;
from openai import OpenAI;
from gtts import gTTS;
import pygame;
import os;

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "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"

def speak_old(text):
    engine.say(text)
    engine.runAndWait()

def speak(text):
    tts = gTTS(text)
    tts.save("AI.mp3")

    # Initialize Pygame Mixer.
    pygame.mixer.init()

    # Load the MP3 File.
    pygame.mixer.music.load("AI.mp3")

    # Play the MP3 File.
    pygame.mixer.music.play()

    # Keep the Program Running Until the Music Stops Playing.
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.music.unload()
    os.remove("AI.mp3")

def aiProcess(command):
    client = OpenAI(
        api_key="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",
    )
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud. Give short responses please",
            },
            {"role": "user", "content": command},
        ],
    )
    return completion.choices[0].message.content

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = MusicLibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r = requests.get(
            f"https://newsapi.org/v2/everything?q=tesla&from=2026-08-14&sortBy=publishedAt&apiKey=32cddf192f26445d900d7284ba75c1c3"
        )
        if r.status_code == 200:
            # Parse the Json Response.
            data = r.json()

            # Extract the Articles.
            articles = data.get("articles", [])

            # Print the HeadLines.
            for article in articles:
                speak(article["title"])
    else:
        # Let OpenAI Handle the Request.
        output = aiProcess(c)
        speak(output)

if __name__ == "__main__":
    speak("Initializing Jarvis...")
    while True:
        # Listen for the Wake Word "Jarvis".
        # Obtain Audio from the Microphone.
        r = sr.Recognizer()
        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if word.lower() == "jarvis":
                speak("Yes, Sir.")

                # Listen for the Command.
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    processCommand(command)
        except Exception as e:
            print("Error; {0}".format(e))