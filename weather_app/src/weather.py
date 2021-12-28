import json
import base64
import requests
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

def print_beginning(title:str="") -> None:
    print("-----------------------------------------")
    print(f'\t\t {title}')
    print("-----------------------------------------")
    print()

def print_ending(ending:str="") -> None:
    print()
    print()
    print(f'\t\t {ending}')
    print("-----------------------------------------")

def _call_gov_weather_api(url_extension) -> req.Request:
    """
        breif: sends an HTTP request to the 'weather.gov' api
        return: request         -  a url content oject containing basic xml data ( needs to be read() and decode() )

        param: url_extension    - the extension with station / city ID to collect the weather from. 
    """

    url = 'http://www.weather.gov/' + url_extension
    try:
        request = req.urlopen(url)
    except err.HTTPError as e:
        print(e, end=' ')
        print(url)
        return None
    return request

def get_gov_weather_by_station(id):
    """
        breif: populates the weather_data dictionary with data provided from the given airport station ID. 
        return: weather_data    - a copy of the weather_data dictionary or None if problem with request.   

        param: id               - the airpoirt station ID to collect the weather from. 
    """
    weather_url = f'xml/current_obs/{id}.xml'
    request = _call_gov_weather_api(weather_url)
    if request is None:
        return None 

    content = request.read().decode()
    xml_root = ET.fromstring(content)

    for data_point in weather_data.keys():
        try:
            weather_data[data_point] = xml_root.find(data_point).text
        except:
            print(f'{data_point} not found in xml file')
            weather_data[data_point] = ' '

    return weather_data

def get_stations_by_state(state_id):
    """
        breif: generates airport station ids given a state in the USA. Used alongside 'get_gov_weather_by_station()' 

        return: tuple: (stations, cities)   - a list of tuples of cities with their matching airport stations found within the state    

        param: state_id                     - the two letter state ID Ex: FL -> Florida, NY -> New York 
    """
    state_id = state_id.lower()
    stations_url = f'xml/current_obs/seek.php?state={state_id}&Find=Find'
    request = _call_gov_weather_api(stations_url)
    content = request.read().decode() #HTML CONTENT

    parser = html_parser()
    parser.feed(content)

    if (len(parser.stations) == len(parser.cities)):
        return parser.stations, parser.cities
    else:
        print('error: parser failed')
        return None

def _call_open_weather_api(url_extension):
    """
        breif: sends an HTTP request to the 'openweathermap.org' api
        return: request         -  a url content oject containing json data

        param: url_extension    - the extension with the city name and country code ('Niagara Falls, CA') to collect the weather from. 
    """

    url = 'http://api.openweathermap.org' + url_extension
    try:
        request = req.urlopen(url)
    except Exception as e:
        print(e, end=' ')
        print(url)
        return None
    return request

def get_open_weather_data(city:str='London, UK'):
    """
        brief: gets the weather data from a city location
        return: a dictionary containing the available weather data 

        parma: city - the city to get the weather data from
    """
    city = city.replace(' ', '%20')
    extension = f'/data/2.5/weather?q={city}&appid={OWM_API_KEY}'
    response = _call_open_weather_api(extension)
    if response is not None:
        data = response.read().decode()
        return json.loads(data)
    else:
        return None 

def get_open_weather_image(weather_icon:str='01d'):
    """
        brief: gets the icon data acording to the icon code specified.
        For full list of icons vist: 'https://openweathermap.org/weather-conditions' 

        return: a byte array of the icon

        param: weather_icon - the icon code to send to the open weather map api 
    """

    url = 'http://openweathermap.org/img/wn/{icon}.png'.format(icon=weather_icon)
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        return base64.encodebytes(response.raw.read()) 
    else:
        return None

def save_base64_image(b64_img_string: str, image_name: str) -> None:
    """
    breif: used to save images that have been encoded with base64 encoding.
    return: None

    param: b64_img_string - the encoded base 64 string.
    param: the name of the image file that gets saved.
    """
    img_data = base64.b64decode(b64_img_string)
    filename = image_name + '.jpg'
    with open(filename, 'wb') as f:
        f.write(img_data)

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
    
    weather_data = get_open_weather_data('Montreal, CA')
    print(weather_data)

    weather_image = get_open_weather_image('01d')
    save_base64_image(weather_image)

    print_ending("GOOD BYE")
    
if __name__ =='__main__':
    main()
