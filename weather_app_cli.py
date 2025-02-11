import requests

# Function to get weather data
def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url)
        response.raise_for_status()  # This will raise an HTTPError for bad responses (4xx or 5xx)
        
        data = response.json()
        if data['cod'] == '404':
            print("City not found. Please try again.")
        else:
            main = data['main']
            weather = data['weather'][0]
            temperature = main['temp']
            pressure = main['pressure']
            humidity = main['humidity']
            description = weather['description']
            
            print(f"\nWeather in {city.capitalize()}:")
            print(f"Temperature: {temperature}°C")
            print(f"Pressure: {pressure} hPa")
            print(f"Humidity: {humidity}%")
            print(f"Description: {description.capitalize()}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")

# Main function to run the app
def main():
    api_key = ""  # Replace with your OpenWeatherMap API key
    while True:
        city = input("\nEnter city name (or type 'exit' to quit): ").strip()
        if city.lower() == 'exit':
            print("Exiting the weather app. Goodbye!")
            break
        elif city:
            get_weather(city, api_key)
        else:
            print("Please enter a city name.")

if __name__ == "__main__":


    main()
