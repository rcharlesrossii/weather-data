import os
import requests


API_KEY = os.environ["api_key"]

# Parameters should be supplied to Weather API as query string parameters
url = "https://api.weatherbit.io/v2.0/forecast/daily"

# Charlotte, NC
charlotte_info = {
    "lat": "35.227085",
    "lon": "-80.843124",
    "key": API_KEY,
    "lang": "en",
    "units": "I",
    "include": "minutely",
}

# Port Washington, WI 
port_washington_info = {
    "lat": "43.3872247",
    "lon": "-87.875644",
    "key": API_KEY,
    "lang": "en",
    "units": "I",
    "include": "minutely",
}

# Create a list to store the keys we want from the response
weather_keys = [
    "datetime",
    "weather",
    "clouds",
    "temp",
    "max_temp",
    "min_temp",
    "rh",
    "pop",
    "precip",
    "snow",
]

def get_weather_data(city):
    """
    Input a dictionary with the proper values needed using the WeatherbitAPI
    guidelines to yield a forecast update for city used in the input.

    More details: https://www.weatherbit.io/api/weather-forecast-16-day

    Args:
        city (dict): A dictionary containing the required information to supply
        the API with for the desired city in which you want the weather
        forecast info for.

    Returns:
        weather_info (dict): Returns the accurate forecast of the city provided
        as the input.
    """
    # Create a dictionary to store the weather info
    weather_info = {}

    # Get the API response using city as the param
    response = requests.get(url, params=city)
    response_data = response.json()["data"][0]

    # Loop through the keys from the response
    for key in weather_keys:
        # Check if the key is in the response_data dictoinary
        if key in response_data:
            # Check if the key is weather, this key is a dictionary
            # We need the value at the dwescription key
            if key == "weather":
                weather_info[key] = response_data[key]["description"]
            else:
                weather_info[key] = response_data[key]
    
    # Return newly populated weather_info
    return weather_info

charlotte_weather = get_weather_data(charlotte_info)
port_washington_weather = get_weather_data(port_washington_info)
