# 🤖 Jarvis Virtual Assistant

A Python-based voice assistant inspired by **Jarvis** that can perform tasks like opening websites, playing music, and fetching the latest news using voice commands.

---

## 🚀 Features

* 🎙️ Voice command recognition
* 🔊 Text-to-speech responses
* 🌐 Open websites (Google, YouTube, LinkedIn, GitHub)
* 🎵 Play music from a custom library
* 📰 Fetch latest news (India headlines)
* 🧠 Modular and scalable code structure

---

## 🧱 Project Structure

```
jarvis/
│── main.py              # Entry point
│── commands.py          # Command handling logic
│── speech.py            # Text-to-speech engine
│── config.py            # API keys and environment config
│── musicLibrary.py      # Music links
│── requirements.txt     # Dependencies
│── .env                 # Secret keys (not pushed to GitHub)
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/sachinsainii/Jarvis-Virtual_Assistant.git
cd Jarvis-Virtual-Assistant
```

---

### 2. Create virtual environment

```bash
python -m venv .venv
```

Activate it:

**Windows:**

```bash
.venv\Scripts\activate
```

**Mac/Linux:**

```bash
source .venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Setup environment variables

Create a `.env` file in root:

```
NEWS_API_KEY=your_news_api_key_here
OPENAI_API_KEY=your_openai_key_here
```

---

## ▶️ Usage

Run the assistant:

```bash
python main.py
```

Say:

* “Jarvis” → to activate
* “Open Google”
* “Play believer”
* “Tell me news”

---

## 🧠 Example Commands

| Command       | Action                 |
| ------------- | ---------------------- |
| Open Google   | Opens Google           |
| Open YouTube  | Opens YouTube          |
| Play believer | Plays song             |
| News          | Reads latest headlines |

---

## 🔐 Security Note

* Do NOT upload `.env` file to GitHub
* Keep API keys private
* `.venv` should be excluded via `.gitignore`

---

## 📦 Requirements

* Python 3.8+
* Microphone access

Main libraries:

* speechrecognition
* pyttsx3
* requests
* python-dotenv

---

## ⚠️ Known Issues

* `PyAudio` installation may fail on Windows
  Fix:

  ```bash
  pip install pipwin
  pipwin install pyaudio
  ```

---

## 🚀 Future Improvements

* 🤖 ChatGPT integration for AI conversations
* 🖥️ GUI interface (Tkinter / PyQt)
* 📱 WhatsApp & Email automation
* 🧠 Wake word detection (Porcupine)
* ⚡ System control (shutdown, open apps)

---

## 👨‍💻 Author

Sachin Saini

---

## ⭐ Contribute

Feel free to fork this repo and improve it!

---

## 📄 License

This project is open-source and available under the MIT License.
