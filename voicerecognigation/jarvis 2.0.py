import speech_recognition as sr
import pyjokes
import pyttsx3
from AppOpener import open
import pywhatkit as kit
import time
import requests
import api
import datetime




#################################################################################################################################
# API Keys
weather_api = api.API_KEY
news_api = api.news_api




#################################################################################################################################
# Main Module
def main():
    wishme()
    uname=username()
    speak ("Hello! I'm Jarvis. Your personal virtual assistant. How can I help you sir?")
    print("Hello! I'm Jarvis.Your personal virtual assistant. How can I help you sir?")
    while True:
        user_input = listen().lower()
        
        if "hello" in user_input:
            speak("Hello! How can I assist you?")
            print("Hello! How can I assist you?")
        elif "tell me a joke" in user_input:
            joke = pyjokes.get_joke()
            speak(joke)
            print(joke)
        elif "news" in user_input:
            news()
        elif "what are you" in user_input:
            print("I am  a programmed virtual assistant made in python language")
            speak("I am  a programmed virtual assistant made in python language")
        elif "who am i" in user_input:
            greet = f"Greetings sir {uname}"
            print(greet)
            speak(greet)
        
        elif "time" in user_input:
            speak(datetime.datetime.now().strftime("%Y %m %d %A  %H:%M:%S "))
            print(datetime.datetime.now().strftime("%Y %m %d %A  %H:%M:%S "))
        elif "weather" in user_input:
            speak("For which city would you like to know the weather? ")
            print("For which city would you like to know the weather? ")
            city = listen().lower()
            speak(get_weather(city))
            print(get_weather(city))
        elif "search" in user_input:
            search()
        elif "open" in user_input:
            speak("Which application you want to open")
            print("Which application you want to open")
            while True:
                msg = listen().lower()
                open(msg.lower(),match_closest=True)
                break
        elif "goodbye"in user_input:
            speak("Goodbye! Have a great day!")
            print("Goodbye! Have a great day!")
            break
        else:
            speak("I'm not sure how to respond to that.")
            print("I'm not sure how to respond to that.")







#################################################################################################################################
# Intro Module
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print("You said:", text)
            return text
        except sr.UnknownValueError:
            print("Sorry, I didn't understand.")
            return ""
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak("Good Morning Sir !")
    elif hour>= 12 and hour<18:
        speak("Good Afternoon Sir !")  
    else:
        speak("Good Evening Sir !")
def username():
    speak("What may i call u sir")
    user_name = listen().lower()
    return user_name






#################################################################################################################################
# Functionalities Module
def news():
    url = f"http://newsapi.org/v2/top-headlines?country=us&apiKey={news_api}"
    response = requests.get(url)
    newspage = response.json()
    article = newspage["articles"]
    results = []
    for ar in article:
        results.append(ar["title"])
    for i in range(5):
        print(i+1,results[i])
        speak(results[i])

def get_weather(city_name):
    base_url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={weather_api}"
    params = {
        "q": city_name,
        "appid": weather_api,
        "units": "metric"  
    }
    response = requests.get(base_url, params=params)
    data = response.json()

    if data["cod"] == 200:
        temperature = data["main"]["temp"]
        description = data["weather"][0]["description"]
        return f"The weather in {city_name} is {description} with a temperature of {temperature:.1f}°C."
    else:
        return "Sorry, I couldn't retrieve the weather information."

def search():
    speak("What do u want to search")
    print("What do u want to search")
    while True:
        msg = listen().lower()
        kit.search(msg)
        time.sleep(5)
        # speak("do you want to search anything else")
        # print("do you want to search anything else")
        # speak("answer in yes or no")
        # print("answer in yes or no")
        # m = listen().lower()
        # while True:
        #     if "yes" in m:      
        #         search()
        #     elif "no"in m:
        #         break
        #     else:
        #         speak("i didn't get your answer")
        #         print("i didn't get your answer")
        #     break
        break




#################################################################################################################################
# Begining
if __name__ == "__main__":
    main()
