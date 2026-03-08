import speech_recognition as sr
import pyttsx3
import pyautogui
import datetime
import os
import time

# ================= VOICE ENGINE =================
engine = pyttsx3.init()
voices = engine.getProperty('voices')

# Female voice (change index if needed)
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)

def speak(text):
    print("JARVIS:", text)
    engine.say(text)
    engine.runAndWait()

# ================= SPEECH RECOGNITION =================
recognizer = sr.Recognizer()

def listen():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            audio = recognizer.listen(source, timeout=8)

        text = recognizer.recognize_sphinx(audio)  # OFFLINE
        print("You:", text)
        return text.lower()

    except Exception:
        return input("Type command: ").lower()

# ================= GREETING =================
def greet():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good morning Yash")
    elif hour < 18:
        speak("Good afternoon Yash")
    else:
        speak("Good evening Yash")

    speak("I am your female Jarvis assistant. How can I help you?")

# ================= PC CONTROL =================
def control_pc(cmd):

    if "open chrome" in cmd:
        speak("Opening Chrome")
        os.system("start chrome")
        return True

    elif "open notepad" in cmd:
        speak("Opening Notepad")
        os.system("start notepad")
        return True

    elif "open calculator" in cmd:
        speak("Opening Calculator")
        os.system("start calc")
        return True

    elif "open explorer" in cmd:
        speak("Opening File Explorer")
        os.system("start explorer")
        return True

    elif "close window" in cmd:
        speak("Closing window")
        pyautogui.hotkey("alt", "f4")
        return True

    elif "screenshot" in cmd:
        speak("Taking screenshot")
        pyautogui.hotkey("win", "shift", "s")
        return True

    elif "volume up" in cmd:
        speak("Increasing volume")
        pyautogui.press("volumeup", presses=5)
        return True

    elif "volume down" in cmd:
        speak("Decreasing volume")
        pyautogui.press("volumedown", presses=5)
        return True

    elif "type" in cmd:
        text = cmd.replace("type", "").strip()
        speak("Typing")
        pyautogui.write(text)
        return True

    return False

# ================= OFFLINE BRAIN =================
def brain(cmd):

    if "hello" in cmd or "hi" in cmd:
        return "Hello Yash, how can I help you?"

    elif "who are you" in cmd:
        return "I am your female Jarvis assistant"

    elif "time" in cmd:
        return datetime.datetime.now().strftime("It is %I:%M %p")

    elif "date" in cmd:
        return datetime.datetime.now().strftime("Today is %A %d %B %Y")

    elif "bye" in cmd or "exit" in cmd or "stop" in cmd:
        speak("Goodbye Yash")
        exit()

    else:
        return "I am an offline assistant. Please give a system command."

# ================= MAIN LOOP =================
def jarvis():
    print("="*50)
    print("FEMALE JARVIS ACTIVATED")
    print("="*50)

    greet()

    while True:
        command = listen()

        if command == "":
            continue

        if control_pc(command):
            continue

        response = brain(command)
        speak(response)

# ================= START =================
if __name__ == "__main__":
    jarvis()
