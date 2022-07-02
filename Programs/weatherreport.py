import requests
import pyttsx3
import speech_recognition as sr

speaker = pyttsx3.init()
voice = speaker.getProperty('voices')
speaker.setProperty('rate', 150)
speaker.setProperty ('voice', voice[1].id)

API_KEY = "44d087acb4c183abdb68c1cd5bc6937a"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?id=524901&"

speaker.say('Please tell us the city name to know weather information')
speaker.runAndWait()
city = input("Enter a city name: ")
speaker.say(f'Did you mean {city}?')
speaker.runAndWait()
request_url = f"{BASE_URL}appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = round(data["main"]["temp"] - 273.15, 2)
    text = f'{city} Weather report : {weather}\nTemperature: {temperature} Degree Celsius'
    print(text)
    speaker.say(text)
    speaker.runAndWait()
else:
    print("An error occurred.")
    speaker.say('Sorry, weather information is not available right now!')
    speaker.runAndWait()