import speech_recognition as sr
import os
import webbrowser
import pyttsx3
import datetime
import wikipedia
import wolframalpha
import requests

# Replace with your actual WolframAlpha app ID
app_id = "Enter Your WolframAlpha app ID"
if app_id is None:
    print("Please set the WOLFRAM_APP_ID environment variable")
    exit(1)

client = wolframalpha.Client(app_id)

def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.6
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            print(f"Error: {e}")
            return "Some Error Occurred. Sorry"

def greet_user():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        say("Good morning!")
    elif hour >= 12 and hour < 18:
        say("Good afternoon!")
    else:
        say("Good evening!")

def process_query(query):
    sites = [["YouTube", "https://www.youtube.com"], ["Wikipedia", "https://www.wikipedia.com"],
             ["Google", "https://www.google.com"]]
    for site in sites:
        if f"open {site[0].lower()}" in query.lower():
            say(f"Opening {site[0]}...")
            webbrowser.open(site[1])
            return

    if "open music" in query.lower():
        music_path = "C:/Users/pravi/Downloads/vinee-heights-126947.mp3"
        if os.path.exists(music_path):
            os.startfile(music_path)
        else:
            say("Music file not found")
        return

    if "the time" in query.lower():
        strf_time = datetime.datetime.now().strftime("%H:%M:%S")
        say(f"The time is {strf_time}")
        return

    if "what is" in query.lower():
        query = query.replace("what is", "")
        try:
            result = wikipedia.summary(query, sentences=2)
            say(result)
        except wikipedia.exceptions.DisambiguationError as e:
            say("I'm not sure what you're referring to. Can you please be more specific?")
        except wikipedia.exceptions.PageError:
            say("I couldn't find any information on that topic.")
        return

    if "calculate" in query.lower():
        query = query.replace("calculate", "")
        try:
            res = client.query(query)
            result = next(res.results).text
            say(result)
        except:
            say("I couldn't calculate that. Please try again.")
        return

    if "how are you" in query.lower():
        say("I'm doing well, thank you for asking!")
        return

    if "who are you" in query.lower():
        say("I am your personal voice assistant, here to help you with any questions or tasks you may have.")
        return

    if "hello" in query.lower() or "hi" in query.lower():
        greet_user()
        return

    if "weather" in query.lower():
        api_key = "Enter Your Weather Api Key"
        base_url = "http://api.openweathermap.org/data/2.5/weather"
        city = query.replace("weather in", "").strip()
        params = {
            "q": city,
            "appid": api_key,
            "units": "metric"
        }
        response = requests.get(base_url, params=params)
        weather_data = response.json()
        if weather_data["cod"] == "404":
            say("City not found. Please try again.")
        else:
            main = weather_data["main"]
            temperature = main["temp"]
            humidity = main["humidity"]
            say(f"The weather in {city} is {temperature} degrees Celsius with {humidity}% humidity.")
        return

    if "news" in query.lower():
        api_key = "Enter Your News Api key"
        base_url = "https://newsapi.org/v2/top-headlines"
        country = "in"
        params = {
            "country": country,
            "apiKey": api_key
        }
        response = requests.get(base_url, params=params)
        news_data = response.json()
        articles = news_data["articles"]
        say("Here are the top news headlines:")
        for article in articles[:5]:
            say(article["title"])
        return

    if "set reminder" in query.lower():
        reminder = query.replace("set reminder to", "").strip()
        reminders = []
        if os.path.exists("reminders.txt"):
            with open("reminders.txt", "r") as f:
                reminders = f.readlines()
        reminders.append(reminder + "\n")
        with open("reminders.txt", "w") as f:
            f.writelines(reminders)
        say(f"Reminder set: {reminder}")
        return

    if "show reminders" in query.lower():
        if os.path.exists("reminders.txt"):
            with open("reminders.txt", "r") as f:
                reminders = f.readlines()
            say("Here are your reminders:")
            for reminder in reminders:
                say(reminder.strip())
        else:
            say("You have no reminders set.")
        return

    say("I didn't understand that. Can you please rephrase your question?")

# Example usage:
if __name__ == "__main__":
    greet_user()
    while True:
        query = take_command()
        process_query(query)

