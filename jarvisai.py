import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib


engine=pyttsx3.init('sapi5')
voices=engine.getProperty("voices")
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour< 12:
        speak("Good morning!!")
    elif hour >=12 and hour< 17:
        speak("Good afternoon")
    else:
        speak("Good evening")
    speak("I am Jarvis. How may i help you sir?")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.....")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"user said {query}")
    except Exception as e:
        print("Say again")
        return "None"
    return query

def sendEmail(to,message):
    server=smtplib.SMTP('server@gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('nikhilkm2696@gmail.com','password')
    server.sendmail('nikhilkm2696@gmail.com',to,message)
    server.close()



if __name__ == '__main__':
    speak("Hello sir!!")
    wishMe()
    while True:
        query=takeCommand().lower()

        if 'wikipedia' in query:
            print("searching wikipedia..")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=1)
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif 'open songs' in query:
            songs_path="C:\\Users\\nikhil\\Desktop\\songs"
            os.startfile(songs_path)

        elif 'what is the time' in query:
            time=datetime.datetime.now().strftime("%H:%M:%S")
            print(f"sir the time is {time}")

        elif 'open instagram' in query:
            webbrowser.open("instagram.com")

        elif 'open chrome' in query:
            chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application"
            os.startfile(chrome_path)

        elif 'send email to nikhil' in query:
            try:
                content=takeCommand()
                to="nikhilkm2696@gmail.com"
                sendEmail(to,content)
                print("email has been sent")
            except Exception as e:
                print(e)
                speak("sorry nikhil ..email has not been sent..some problem occured")

        elif 'quit' in query:
            exit()


