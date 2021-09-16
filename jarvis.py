import pyttsx3
import requests, json
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import wolframalpha
import shutil
import pyjokes
from googlesearch import *
import time

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',175)
engine.setProperty('volume',2.0)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        g= "Good morning Sir...I am here to assist you. Ask me if you need any help"
        print(g)
        speak(g)

    elif hour>=12 and hour<18:
        g= "Good morning Sir...I am here to assist you. Ask me if you need any help"
        print(g)
        speak(g)

    else:
        g= "Good evening Sir...I am here to assist you. Ask me if you need any help"
        print(g)
        speak(g)
    

def start():
        s = "Hello Sir,How may i help you?"
        print(s)
        speak(s)

def takeCommand():
    #It takes microphone input from the user and return tring output
    r =sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-IN')
        print(f"User said: {query}")

    except Exception as e:
        print(e)
        print("Sorry sir i didn't get you,please speak again...")
        return "None"
    return query

    def wait():
        while True:
            time.sleep()



def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your_mail@gmail.com', 'password')
    server.sendmail('reciever mail address', to,content)
    server.close()

#def MainClass():
if __name__ == "__main__":
    my_name= "Gaganpreet Singh" 

    while True:
        WishMe()
        input("press ENTER to continue...")
        
        wake=takeCommand().lower()
        if "jarvis" in wake:
            waked=True
            start()
            break
        else:
            continue
            
    while waked:
        query = takeCommand().lower()
        #logic for exceuting tasks based on query
        if 'wikipedia' in query:
            try:
                speak("Searching Wikipedia...")
                query = query.replace("wikipedia","")
                result = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(result)
                speak(result)
            except Exception as e:
                speak("not found anything regarding search")
                print(e)

        elif "calculate" in query or "what is" in query or "who is" in query:
            try:
                app_id = "V6KA96-5Q8LRAWHJG"
                client = wolframalpha.Client(app_id)
                query = query.replace("calculate","")
                query = query.replace("what is","")
                query = query.replace("who is","")
                result = client.query(query)
                answer = next(result.results).text
                print("The answer is " + answer)
                speak("The answer is " + answer)
                
            except Exception:
                speak("sorry sir,answer not found")

        elif "who are you" in query:
            print("I am jarvis an A I based computer program but I can help you alot like your friend :) ")
            speak("I am jarvis an A I based computer program but I can help you alot like your friend")

        elif "who made you" in query or "who created you" in query:
            speak("I am jarvis created by gaganpreet singh")
            print("I am jarvis created by Gaganpreet Singh")
       
        elif "who i am" in query:
            speak("If you talk then definately you are human.")
        
        elif "how are you" in query: 
            speak("I am fine" ) 
            speak("what about you, Sir") 

        elif 'fine' in query or "good" in query: 
            speak("It's good to know that your fine") 

        elif 'open youtube' in query or "go to youtube" in query:
            speak("openning youtube")
            webbrowser.open("youtube.com")

        elif 'open google' in query or "go to google" in query:
            speak("openning google")
            webbrowser.open("google.com")
        
        elif 'open facebook' in query or "go to my facebook" in query:
            speak("openning facebook")
            webbrowser.open("https://www.facebook.com/gagan.pannu.121/")
        
        elif 'open instagram' in query or "go to instagram" in query:
            speak("openning Instagram")
            webbrowser.open("https://www.instagram.com/")
        
        elif 'open amazon' in query or "go to amazon" in query:
            speak("openning Amazon")
            webbrowser.open("https://www.amazon.in/?ref_=nav_signin&")
        
        elif 'open stackoverflow' in query:
            speak("openning stackoverflow")
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query or "play songs" in query:
            music = 'D:\\Songs'
            songs = os.listdir(music)
            print(songs)
            os.startfile(os.path.join(music,songs[0]))
            
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir, the time is {strTime}")

        elif 'vs code' in query:
            speak("opening visual studio code")
            codePath = "C:\\Users\\GAGAN\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        
        elif 'send email' in query:
            try:
                speak("to whom do you want to send email sir?")
                to = input()
                speak("what you want to send sir?")
                content = takeCommand()
                sendEmail(to, content)
                print("Email has been sent!")
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Sir! I am not able to send email")

        elif "what's my name" in query:
            print("You are my creater and your name is "+my_name)
            speak("You are my creater and your name is "+my_name)
        
        elif "change my name" in query:
            print("Alright Sir! What should I call You?")
            speak("Alright Sir! What should I call You?")
            a=takeCommand()
            my_name,a =a,my_name
            print("Your name has been changed sir!")
            speak("Your name has been changed sir!")
            print(my_name)
        
        elif "what's your name" in query or "what is your name" in query:
            print("My creater gives me name Jarvis, And I like my name so much")
            speak("My creater gives me name Jarvis, And I like my name so much")

        elif "well done" in query or "you are so good assistant" in query or "you are awesome" in query:
            speak("I am happy to help you sir!")
        
        elif "bored" in query:
            speak("I can help you sir to make your mood better..")
            speak("I can play song..  or I can play movie for you or I can tell you some jokes ")

        elif "change your name" in query:
            speak("sorry sir! my creater gives me a very nice name and he don't want anyone to change my name")

        elif 'on google' in query or "at google" in query:
            query = query.replace("on google","")
            query = query.replace("at google","")
            for url in search(query, tld="com", num=1, stop = 1, pause = 2):
                speak("searching on google")
                webbrowser.open("https://google.com/search?q=%s" % query)

        elif 'powerpoint' in query:
            speak("opening powerpoint")
            codePath1 = "C:\\Program Files\\Microsoft Office\\root\Office16\\POWERPNT.EXE"
            os.startfile(codePath1)
        
        elif 'paint' in query:
            speak("opening paint")
            codePath1 = "%windir%\\system32\\mspaint.exe"
            os.system(codePath1)
       
        elif 'excel' in query:
            speak("opening microsoft excel")
            codePath1 = "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
            os.startfile(codePath1)
        
        elif ' microsoft word' in query:
            speak("opening microsoft word")
            codePath1 = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
            os.startfile(codePath1)

        elif 'open control panel' in query:
            speak("opening Control Panel")
            codePath1 = "Control Panel"
            os.system(codePath1)
        
        elif 'joke' in query:
            print(pyjokes.get_joke())
            speak(pyjokes.get_joke()) 

        elif "shutdown" in query:
            print("Shutting down sir :)")
            speak("Shutting down sir")
            break

        elif "sleep mode" in query:
            waked=False
            speak("Going to sleep mode")
        
        else:
            continue
        
        