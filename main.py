import speech_recognition as sr
from speech import speak
from commands import process_command


def listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)

        try:
            audio = r.listen(source, timeout=5)
            command = r.recognize_google(audio)
            print("You said:", command)
            return command

        except sr.WaitTimeoutError:
            return ""
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that")
            return ""
        except Exception:
            speak("Error occurred")
            return ""


def main():
    speak("Jarvis activated")

    while True:
        command = listen()

        if command:
            if "jarvis" in command.lower():
                speak("Yes?")
                command = listen()
                process_command(command)


if __name__ == "__main__":
    main()






