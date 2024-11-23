import requests

def get_weather(city, api_key):
    """
    Fetches current weather for the specified city using OpenWeatherMap API.

    :param city: str, name of the city
    :param api_key: str, API key for OpenWeatherMap
    :return: None
    """
    try:
        # API endpoint and parameters
        url = "http://api.openweathermap.org/data/2.5/weather"
        params = {"q": city, "appid": api_key, "units": "metric"}  # Units in Celsius

        # Sending GET request
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise exception for HTTP errors

        # Parsing JSON response
        data = response.json()
        weather = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        city_name = data["name"]

        # Display weather info
        print(f"Weather in {city_name}: {weather.capitalize()}")
        print(f"Temperature: {temperature}°C")

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Error occurred: {req_err}")
    except KeyError:
        print("City not found or invalid API key. Please try again.")

# Main program
if __name__ == "__main__":
    # Replace with your OpenWeatherMap API key
    API_KEY = "your_api_key_here"
    city_name = input("Enter the city name to check the weather: ").strip()
    get_weather(city_name, API_KEY)
