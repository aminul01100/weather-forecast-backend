import openmeteo_requests

import requests_cache
import pandas as pd
from retry_requests import retry

# Setup the Open-Meteo API client with cache and retry on error
cache_session = requests_cache.CachedSession('.cache', expire_after=3600)
retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
openmeteo = openmeteo_requests.Client(session=retry_session)

url = "https://api.open-meteo.com/v1/forecast"


# there might a better way to do this form the docs if we want it for actual usage but this is sufficient for now
def get_temperature_list(params):
    response = openmeteo.weather_api(url, params=params)
    temperature_list = response[0].Hourly().Variables(0).ValuesAsNumpy().tolist()
    return temperature_list


def get_daily_temperature(params):
    response = openmeteo.weather_api(url, params=params)
    daily_list = response[0].Daily().Variables(0).ValuesAsNumpy().tolist()
    return daily_list[0]
