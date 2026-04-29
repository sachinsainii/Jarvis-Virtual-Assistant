import webbrowser
import requests
from speech import speak
import musicLibrary
from config import NEWS_API_KEY


commands = {
    "open google": "https://google.com",
    "open youtube": "https://youtube.com",
    "open linkedin": "https://linkedin.com",
    "open github": "https://github.com",
}


def open_website(command):
    for key in commands:
        if key in command:
            webbrowser.open(commands[key])
            speak(f"Opening {key}")
            return True
    return False


def play_music(command):
    song = command.replace("play", "").strip()

    if song in musicLibrary.music:
        webbrowser.open(musicLibrary.music[song])
        speak(f"Playing {song}")
    else:
        speak("Song not found")


def get_news():
    url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API_KEY}"

    try:
        response = requests.get(url)
        data = response.json()

        articles = data.get("articles", [])

        if not articles:
            speak("No news available")
            return

        for i, article in enumerate(articles[:5]):
            speak(article["title"])

    except Exception as e:
        speak("Error fetching news")


def process_command(command):
    command = command.lower()

    if open_website(command):
        return

    elif command.startswith("play"):
        play_music(command)

    elif "news" in command:
        get_news()

    else:
        speak("I didn't understand that command")