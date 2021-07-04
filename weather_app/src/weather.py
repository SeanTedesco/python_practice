import json
import urllib.request as req
import urllib.error as err
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from datetime import datetime
from API_KEY import OWM_API_KEY

class html_parser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stations = []
        self.cities = []
        self.grab_data = False

    def handle_starttag(self, tag, attrs):
        for attr in attrs:
            if 'display.php?stid=' in str(attr):
                cleaned_attr = str(attr).replace("('href', 'display.php?stid=", '').replace("')", '')
                self.stations.append(cleaned_attr)
                self.grab_data = True
    
    def handle_data(self, data):
        if self.grab_data:
            self.cities.append(data)
            self.grab_data = False

weather_data = {
    'observation_time': '',
    'weather': '',
    'temp_c': '',
    'dewpoint_c': '',
    'relative_humidity': '',
    'dewpoint_f': '',
    'dewpoint_string': '',
    'icon_url_base': '',
    'icon_url_name': '',
    'latitude': '',
    'longitude': '',
    'location': '',
    'observation_time_rfc822': '',
    'pressure_in': '',
    'pressure_mb': '',
    'pressure_string': '',
    'station_id': '',
    'suggested_pickup': '',
    'suggested_pickup_period': '',
    'temp_f': '',
    'temperature_string': '',
    'visibility_mi': '',
    'wind_degrees': '',
    'wind_dir': '',
    'wind_mph': '',
    'wind_string': '',
}

def print_beginning(title:str=""):
    print("-----------------------------------------")
    print(f'\t\t {title}')
    print("-----------------------------------------")
    print()

def print_ending(ending:str=""):
    print()
    print()
    print(f'\t\t {ending}')
    print("-----------------------------------------")

def _call_weather_api(url_extension):
    url = 'http://www.weather.gov/xml/current_obs/' + url_extension
    try:
        request = req.urlopen(url)
    except err.HTTPError as e:
        print(e, end=' ')
        print(url)
        return None
    return request

def get_weather_by_station(id):
    weather_url = f'{id}.xml'
    request = _call_weather_api(weather_url)
    content = request.read().decode()
    xml_root = ET.fromstring(content)

    for data_point in weather_data.keys():
        try:
            weather_data[data_point] = xml_root.find(data_point).text
        except:
            print(f'{data_point} not found in xml file')

    return weather_data

def get_stations_by_state(state_id):
    state_id = state_id.lower()
    stations_url = f'seek.php?state={state_id}&Find=Find'
    request = _call_weather_api(stations_url)
    content = request.read().decode() #HTML CONTENT

    parser = html_parser()
    parser.feed(content)

    if (len(parser.stations) == len(parser.cities)):
        return parser.stations, parser.cities
    else:
        print('error: parser failed')
        return None

def _call_open_weather_api(url_extension):
    url = 'http://api.openweathermap.org' + url_extension
    try:
        request = req.urlopen(url)
    except err.HTTPError as e:
        print(e, end=' ')
        print(url)
        return None
    return request

def get_open_weather_data(city:str='London, UK'):
    city = city.replace(' ', '%20')
    extension = f'/data/2.5/weather?q={city}&appid={OWM_API_KEY}'
    response = _call_open_weather_api(extension)
    if response is not None:
        data = response.read().decode()
        return json.loads(data)

def get_open_weather_image(weather_icon:str='04n'):
    extension = f'/img/w/{weather_icon}.png'
    img = _call_open_weather_api(extension)
    return img

def kelvin_to_celcius(temp_k):
    return "{:.1f}".format(temp_k - 273.15)

def kelvin_to_fahrenheit(temp_k):
    return "{:.1f}".format( (temp_k - 273.15)*1.8000 + 32.00 )

def unix_to_datetime(unix_time):
    return datetime.fromtimestamp(int(unix_time)).strftime('%Y-%m-%d %H:%M:%S')

def meter_to_miles(meter):
    return "{:.2f}".format((meter*0.00062137))

def mps_to_mph(meter_second):
    return "{:.1f}".format((meter_second*2.23693629))

def main():
    print_beginning("WEATHER APP")

    get_open_weather_data()


    print_ending("GOOD BYE")
    
if __name__ =='__main__':
    main()