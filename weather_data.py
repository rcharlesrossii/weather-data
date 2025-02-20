from weatherbit_api_key import api_key
import requests


# Parameters should be supplied to Weather API as query string parameters
url = "https://api.weatherbit.io/v2.0/forecast/daily"

# Charlotte, NC
params = {
    "lat": "35.227085",
    "lon": "-80.843124",
    "key": api_key,
    # "lang": "en",
    # "units": "I",
    "include": "minutely",
}

# Port Washington, WI 
# params = {
#     "lat": "43.3872247",
#     "lon": "-87.875644",
#     "key": api_key,
#     # "lang": "en",
#     # "units": "I",
#     "include": "minutely",
# }

response = requests.get(url, params=params)

# Example request
# https://api.weatherbit.io/v2.0/current?lat=35.7796&lon=-78.6382&key=API_KEY&include=minutely

# print(response.url, "\n")
# print(response.status_code, "\n")
# print(response.headers, "\n")
# print(response.encoding, "\n")
# print(response.text, "\n")
print(response.json(), "\n")

"""
Desired keys (within the data key, it is a list with dictionary values for the last 16 days)"
clouds, clouds_hi, clouds_low, datetime, high_temp, low_temp, max_temp, min_temp, precip, rh snow, snow_depth, weather -> description 
"""
