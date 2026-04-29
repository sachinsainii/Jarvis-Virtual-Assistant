import webbrowser
import requests
from speech import speak
import musicLibrary
from config import NEWS_API_KEY
from client import ask_ai
from memory import remember, recall


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
            return "No news available"

        headlines = []
        for article in articles[:5]:
            headlines.append(article["title"])

        return "\n".join(headlines)

    except:
        return "Error fetching news"

def process_command(command):
    command = command.lower()

    if "open google" in command:
        webbrowser.open("https://google.com")
        return "Opening Google"

    elif "open youtube" in command:
        webbrowser.open("https://youtube.com")
        return "Opening YouTube"

    elif command.startswith("play"):
        song = command.replace("play", "").strip()
        if song in musicLibrary.music:
            webbrowser.open(musicLibrary.music[song])
            return f"Playing {song}"
        return "Song not found"

    elif "news" in command:
        return get_news()

    elif "my name is" in command:
        name = command.replace("my name is", "").strip()
        remember("name", name)
        return f"Nice to meet you, {name}"

    elif "what is my name" in command:
        name = recall("name")
        if name:
            return f"Your name is {name}"
        return "I don't know your name yet"

    elif "remember that" in command:
        info = command.replace("remember that", "").strip()
        remember("note", info)
        return "I will remember that"

    elif "what did i say" in command:
        note = recall("note")
        if note:
            return f"You said: {note}"
        return "I don't remember anything"

    # AI fallback
    else:
        return ask_ai(command)