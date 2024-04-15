import requests
import json
import pyttsx3

def get_weather(city):
    key = "92a9d3190d13274243863b0906f698ba"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}"
    r = requests.get(url)
    
    if r.status_code == 200:
        wdic = json.loads(r.text)
        temp = round(wdic["main"]["temp"] - 273.15, 2)
        humidity = wdic["main"]["humidity"]
        pressure = wdic["main"]["pressure"]
        country = wdic["sys"]["country"]
        
        return {
            "country": country,
            "temp": temp,
            "humidity": humidity,
            "pressure": pressure
        }
    else:
        return None

def say(text, rate=170, voice_id='com.apple.speech.synthesis.voice.Alex'):
    speak = pyttsx3.init()
    speak.setProperty('rate', rate)
    if voice_id:
        speak.setProperty('voice', voice_id)
    speak.say(text)
    speak.runAndWait()

city = input("Enter the name of the city: ")
weather_data = get_weather(city)

if weather_data:
    text = f"The current weather in {city} is {weather_data['temp']} degrees, humidity is {weather_data['humidity']}, and pressure is {weather_data['pressure']}."
else:
    text = "Please enter a valid city name."

say(text)
