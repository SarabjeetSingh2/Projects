import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia

engine=pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
voiceRate=110
engine.setProperty('rate',voiceRate)


def speak(sound):
    engine.say(sound)
    engine.runAndWait()


def time():
    ttime = datetime.datetime.now().strftime("%I:%M:%S")
    speak(ttime)

def date():
    year=(datetime.datetime.now().year)
    month=(datetime.datetime.now().month)
    day=(datetime.datetime.now().day)
    speak("The current date is :")
    speak(day)
    speak(month)
    speak(year)

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening ...........")
        audio = r.listen(source)

    try:
        print("recognizing.......")
        query=r.recognize_google(audio,)
        print("you said : {}".format(query))
    except Exception as e:
        print(e)
        return "None"
 
    return query

speak("HI")
speak("I am an assistant created by Sarabjeet Singh how can i help you ")

if __name__ =="__main__":
    while True:
        query=takecommand().lower()
        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif "offline" in query:
            quit()
        elif "search" in query:
            speak("searching")
            query=query.replace("search","")
            result=wikipedia.summary(query,sentences = 1)
            speak(result)



