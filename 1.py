import requests

def get_weather(city):
    api_url = f"https://wttr.in/{city}?format=j1"
    
    response = requests.get(api_url)
    data = response.json()
    
    # Extract important info
    area = data['nearest_area'][0]['areaName'][0]['value']
    region = data['nearest_area'][0]['region'][0]['value']
    country = data['nearest_area'][0]['country'][0]['value']
    temperature = data['current_condition'][0]['temp_C']
    weather_desc = data['current_condition'][0]['weatherDesc'][0]['value']

    print(f"\nWeather Report for {area}, {region}, {country}")
    print("----------------------------------------")
    print(f"Temperature: {temperature}°C")
    print(f"Condition: {weather_desc}")
    print("----------------------------------------")

# Get input from user
city_name = input("Enter city name: ")
get_weather(city_name)
