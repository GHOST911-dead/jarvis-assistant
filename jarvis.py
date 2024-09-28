import datetime
import pyttsx3
import speech_recognition as sr
import wikipedia
import os
import platform
import psutil
import time
import requests
import json
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import wmi
import random


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Jarvis Sir. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query
def get_battery_status():
    """Function to get the battery status."""
    battery = psutil.sensors_battery()
    return battery.percent

def monitor_battery():
    """Function to monitor battery and alert when it goes below 20%."""
    while True:
        battery_percentage = get_battery_status()
        if battery_percentage <= 20:
            speak("Sir, my battery is low. Please charge me as soon as possible.")
        time.sleep(60)  # Check every minute

application_paths = {
    'notepad': 'C:\\Windows\\system32\\notepad.exe',
    'calculator': 'C:\\Windows\\system32\\calc.exe',
    'visual studio': 'C:\\Users\\Khanjan\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe',
    'chrome': 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
    'brave': 'C:\\Users\\Khanjan\\AppData\\Local\\BraveSoftware\\Brave-Browser\\Application\\brave.exe',
    
}

def open_application(app_name):
    """Function to open an application by name."""
    app_name = app_name.lower()
    app_path = application_paths.get(app_name)
    
    if app_path:
        os.startfile(app_path)
        speak(f"Opening {app_name}")
    else:
        speak(f"Sorry, I don't know how to open {app_name}")

def fetch_random_joke():
    """Function to fetch a random joke from the API."""
    try:
        response = requests.get("https://official-joke-api.appspot.com/random_joke")
        data = response.json()
        return f"{data['setup']} {data['punchline']}"
    except Exception as e:
        print("Failed to fetch joke:", e)
        return None

def check_connected_devices():
    """Function to check if any devices are connected to the system."""
    connected_devices = False
    
    if platform.system() == "Windows":
        c = wmi.WMI()
        for usb in c.Win32_USBControllerDevice():
            connected_devices = True
            break

    if connected_devices:
        speak("Yes, there are devices connected to your system.")
    else:
        speak("No, there are no devices connected to your system.")

def post_data_to_api(data):
    """Function to post data to a sample API."""
    api_url = "https://jsonplaceholder.typicode.com/posts"
    payload = {
        "title": "My Post",
        "body": data,
        "userId": 1
    }
    try:
        response = requests.post(api_url, json=payload)  # Use json parameter directly
        if response.status_code == 201:
            speak("Data successfully posted to the API.")
            print(f"Response from API: {response.json()}")
        else:
            speak("Failed to post data to the API.")
    except Exception as e:
        print(f"Error occurred: {e}")
        speak("Could not complete the API request.")
def generate_web_series_suggestion():
    """Function to suggest a random web series with a plot summary."""
    # List of web series with their plot summaries
    web_series_list = {
        "Stranger Things": "A group of kids uncover supernatural mysteries in their town while searching for their missing friend.",
        "The Crown": "This series chronicles the reign of Queen Elizabeth II and the events that shaped the second half of the 20th century.",
        "Breaking Bad": "A high school chemistry teacher turned methamphetamine manufacturer partners with a former student to secure his family's future.",
        "Game of Thrones": "Noble families vie for control of the Iron Throne in a fantasy realm filled with political intrigue and dragons.",
        "The Witcher": "Geralt of Rivia, a monster hunter, navigates a world filled with deadly beasts and political turmoil as he seeks his destiny.",
        "Money Heist": "A criminal mastermind leads a group of robbers in a meticulously planned heist on the Royal Mint of Spain.",
        "The Mandalorian": "In the Star Wars universe, a lone bounty hunter navigates the outer reaches of the galaxy, protecting a mysterious child.",
        "Dark": "A family saga with a supernatural twist that spans several generations, revealing secrets across time and space.",
        "The Office": "A mockumentary-style comedy that follows the daily lives of office employees working at Dunder Mifflin.",
        "Friends": "Six friends navigate the ups and downs of life, love, and friendship in New York City.",
        "The Queen's Gambit": "An orphaned chess prodigy rises to prominence while battling addiction and personal issues in the male-dominated world of chess.",
        "Peaky Blinders": "Set in post-World War I Birmingham, a gangster family fights to expand their criminal empire amid rising tensions.",
        "Fargo": "Inspired by the Coen Brothers' film, this anthology series features various tales of crime, morality, and dark humor in the Midwest.",
        "Ozark": "A financial planner relocates his family to the Ozarks after a money-laundering scheme goes wrong, navigating dangerous criminal elements.",
        "Narcos": "The story of the rise and fall of drug kingpin Pablo Escobar and the DEA agents determined to bring him down.",
        "Sex Education": "A socially awkward high school student starts an underground sex therapy clinic to help his classmates navigate their relationships.",
        "The Haunting of Hill House": "A family confronts haunting memories of their old home and the terrifying events that drove them away.",
        "The Boys": "In a world where superheroes exist, a group of vigilantes aims to take down corrupt heroes who abuse their powers.",
        "Succession": "A media mogul's family battles for control of the family business amid dysfunction, betrayal, and personal conflicts."
    }
    
    # Fetch a random web series and its plot
    suggested_series = random.choice(list(web_series_list.keys()))
    plot_summary = web_series_list[suggested_series]
    
    return suggested_series, plot_summary

def suggest_web_series_and_speak():
    """Function to suggest a web series and speak its plot."""
    web_series, plot = generate_web_series_suggestion()
    print(f"Suggested Web Series: {web_series}")
    speak(f"Suggested web series is {web_series}. {plot}")
    speak(f"Suggested web series is {web_series}. {plot}")

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        elif 'suggest a web series'in query:
            suggest_web_series_and_speak()
        elif 'open d drive' in query:
            os.startfile('D:\\')

        elif 'movie' in query:
         speak("Enjoy your movie, sir.")
         os.startfile('E:\\This is for entertainment')

        elif 'hello' in query:
            speak("Hello Sir or Mam, I am Jarvis, Khanjan's Partner.")

        elif 'what is my battery' in query:
            battery_percentage = get_battery_status()
            speak(f"Sir, your battery is at {battery_percentage} percent.")
            print(f"Sir, your battery is at {battery_percentage} percent.")

        elif 'open' in query:
            app_name = query.replace('open', '').strip()
            open_application(app_name)

        elif 'tell me a joke' in query:
            joke = fetch_random_joke()
            if joke:
                speak("Here's a joke for you:")
                print(joke)
                speak(joke)
                speak("Ha ha ha, very funny isn't it?")
            else:
                speak("Sorry, I couldn't fetch a joke at the moment.")

        elif 'post data' in query:
            speak("What data would you like to post to the API?")
            data_to_post = takeCommand()
            post_data_to_api(data_to_post)


        
        
