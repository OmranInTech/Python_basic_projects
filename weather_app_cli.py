import requests

API_BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
UNITS = "metric"
EXIT_COMMAND = "exit"
NOT_FOUND_CODE = "404"

def build_weather_api_url(city_name: str, api_key: str) -> str:
    return f"{API_BASE_URL}?q={city_name}&appid={api_key}&units={UNITS}"

def fetch_weather_data(city_name: str, api_key: str) -> dict:
    """Fetches weather data from the API."""
    try:
        response = requests.get(build_weather_api_url(city_name, api_key))
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as error:
        print(f"[Error] Failed to retrieve weather data: {error}")
        return {}

def is_city_not_found(api_response: dict) -> bool:
    return api_response.get('cod') == NOT_FOUND_CODE

def display_weather_report(city_name: str, weather_data: dict):
    """Displays the weather report in a readable format."""
    main_data = weather_data.get('main', {})
    weather_description = weather_data.get('weather', [{}])[0].get('description', 'N/A')

    print(f"\nWeather Report for {city_name.title()}:")
    print(f"Temperature: {main_data.get('temp', 'N/A')}°C")
    print(f"Pressure: {main_data.get('pressure', 'N/A')} hPa")
    print(f"Humidity: {main_data.get('humidity', 'N/A')}%")
    print(f"Description: {weather_description.capitalize()}")

def prompt_for_city_name() -> str:
    return input("\nEnter city name (or type 'exit' to quit): ").strip()

def run_weather_application():
    """Main loop for the weather app."""
    api_key = ""  # Replace with your real OpenWeatherMap API key

    while True:
        city_name = prompt_for_city_name()

        if city_name.lower() == EXIT_COMMAND:
            print("Exiting the weather app. Goodbye!")
            break

        if not city_name:
            print("⚠️  City name cannot be empty.")
            continue

        weather_data = fetch_weather_data(city_name, api_key)

        if not weather_data:
            continue  # Error already printed
        if is_city_not_found(weather_data):
            print("❌ City not found. Please try again.")
            continue

        display_weather_report(city_name, weather_data)

if __name__ == "__main__":
    run_weather_application()
