import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!!")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon!!")
    else:
        speak("Good evening!!")
    speak("I am PyJarvis sir,please tell me how may i help you?")


def takeCommand():
    '''
    It takes microphone input from the user and returns string output
    '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.phrase_threshold = 0.3
        # r.energy_threshold = 300
        audio = r.listen(source)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio)
        print(f"user said :{query}\n")
    except Exception as e:
        print(e)
        print("say that again please....")
        return "None"
    return query


if __name__ == '__main__':

    wishMe()
    while True:
        query = takeCommand().lower()
        if "wikipedia" in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia", "")
            print(query)
            results = wikipedia.summary(query, sentences=2)
            print(f"results: {results}")
            speak("According to wikipedia...")
            speak(results)
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        elif "open google" in query:
            webbrowser.open("google.com")
        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")
        elif "open udemy" in query:
            webbrowser.open("udemy.com")
        elif "play cartoon" in query:
            webbrowser.open("cartoon.com")
        elif "play music" in query:
            music_dir = "E:\\songs"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"sir,the time is {strTime}")
        elif "open vs code" in query:
            v_s_codePath="C:\\Users\\lenovo\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(v_s_codePath)
        elif "control panel" in query:
            os.system("control panel")
        elif "command prompt" in query:
            os.system('cmd /k ')