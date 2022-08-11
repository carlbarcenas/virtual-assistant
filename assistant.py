import pyttsx3  # Text-to-speech
from vosk import Model, KaldiRecognizer # Speech Recognition
import os
import datetime
from calendar import day_name

# Basic initializations
currUser = "Carl"

# TTS Initialization
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
newVoiceRate = 165
engine.setProperty('rate', newVoiceRate)

# Speech Recognition initialization
model = Model(os.getcwd() + "\\packages\\vosk-model-en-us-0.22")
recognizer = KaldiRecognizer(model, 16000)

#================ FUNCTIONS ====================
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    currentTime = datetime.datetime.now().strftime("%I:%M %p")
    speak(currentTime)

def date():
    currentDate = datetime.date.today()
    month = currentDate.strftime("%B")
    day = str(currentDate.strftime("%d"))
    weekday = day_name[currentDate.weekday()]
    speak("It is " + weekday + ", " + month + day)

def greetings(user):
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour <= 12:
        speak("Good morning, " + user)
    elif hour > 12 and hour < 18:
        speak("Good afternoon, " + user)
    elif hour >= 18 and hour <= 24:
        speak("Good evening, " + user)
    else:
        speak("Good night, " + user)

    speak("Welcome back!")
    date()
    time()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1   # Waits for 1 second
        audio = r.listen(source)

    try:
        print("Recognizing...")
        #query = r.recognize_google(audio, 'en=US')
        query = r.recognize_google()
        print(query)
    except Exception as e:
        print(e)
        speak("Say that again please?")
        return "None"

    return query


# ================= MAIN LOOP ==================

if __name__ == "__main__":
    greetings(currUser)

    while True:
        query = takeCommand().lower
        print(query)

        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif "offline" in query:
            quit()