import requests

api_key = 'e086426522fd7c9072b3a24ba190705d'

user_input = input("Enter city : ")

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

if weather_data.json()['cod'] == '404':
    print("No City Found")
else:
    weather = weather_data.json()['weather'][0]['main']
    temp = (weather_data.json()['main']['temp'])
    humidity = round(weather_data.json()['main']['humidity'])
    feels = round(weather_data.json()['main']['feels_like'])
    wind = round(weather_data.json()['wind']['speed'])
    clouds = round(weather_data.json()['clouds']['all'])
    name = (weather_data.json()['name'])
    
    temp = round(((int(temp)-32)*5)/9)  
    feels = round(((int(feels)-32)*5)/9) 
 

    print(f"The weather in {name} is {weather} with {clouds}% cloud. The temperature in {name} is {temp}ºC but it feels like {feels}ºC because of {humidity}% humidity. The wind is blowing with speed {wind}km/hr. Thank you.")
