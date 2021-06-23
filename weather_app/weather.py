
import urllib.request as req
import xml.etree.ElementTree as ET

weather_data = {
    'dewpoint_c': '',
    'dewpoint_f': '',
    'dewpoint_string': '',
    'icon_url_base': '',
    'icon_url_name': '',
    'latitude': '',
    'longitude': '',
    'location': '',
    'observation_time': '',
    'observation_time_rfc822': '',
    'pressure_in': '',
    'pressure_mb': '',
    'relative_humidity': '',
    'station_id': '',
    'suggested_pickup': '',
    'suggested_pickup_period': '',
    'temp_c': '',
    'temp_f': '',
    'temperature_string': '',
    'visibility_mi': '',
    'weather': '',
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

def parse_location(location:str=""):
    if not location or not location.strip():
        raise ValueError("error: no location given!")
    
    location = location.lower().strip()
    if ',' not in location:
        raise ValueError("error: seperate city, state, and country by commas!")
    location = location.split(',')

    city, state, country = '', '', 'us'
    if len(location) == 1:
        city = location[0].strip()
    elif len(location) == 2:
        city = location[0].strip()
        country = location[1].strip()
    elif len(location) == 3:
        city = location[0].strip()
        state = location[1].strip()
        country = location[2].strip()
    else:
        raise ValueError("error: unexpected input for location!")

    return Location(city, state, country)

def call_weather_api(station_id:str='KLAX'):
    url = f'http://www.weather.gov/xml/current_obs/{station_id}.xml'
    request = req.urlopen(url)
    content = request.read().decode()
    xml_root = ET.fromstring(content)

    for data_point in weather_data.keys():
        try:
            weather_data[data_point] = xml_root.find(data_point).text
        except:
            print(f'{data_point} not found in xml file')

    return weather_data
    

def main():
    print_beginning("WEATHER APP")

    foo = call_weather_api()
    print(foo)

    print_ending("GOOD BYE")
    
if __name__ =='__main__':
    main()