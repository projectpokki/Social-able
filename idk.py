import requests

def get_user_permission():
    response = input("Do you allow me to check the weather for you? (yes/no): ").strip().lower()
    return response == 'yes'

def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        desc = data['weather'][0]['description']
        return f"The temperature in {city} is {temp}°C with {desc}."
    else:
        return "Sorry, I couldn't retrieve the weather data."

def main():
    api_key = "YOUR_OPENWEATHERMAP_API_KEY"  # Replace with your actual key
    if get_user_permission():
        city = input("Please enter your city: ").strip()
        weather_report = get_weather(city, api_key)
        print(weather_report)
    else:
        print("Okay, I won't check the weather without your permission.")

if __name__ == "__main__":
    main()
