import requests
from requests import exceptions
import collections
import json

api_url = 'https://movieservice.talkpython.fm/api/'

MovieResult = collections.namedtuple('MovieResult', 'imdb_code, imdb_score, rating, title, director, year, keywords, duration, genres')

def find_movies(search_term) -> MovieResult:
    """given a search term, return a list of named tuples of the movies found"""

    if not search_term or not search_term.strip():
        raise ValueError("error: search text is required")

def call_api_for_search_term(search_term):
    search = api_url + 'search/' + search_term
    return call_api(search)

def call_api(url):
    """calls the url given and returns json data if ok, raises a status error if invalid url."""

    try:
        request = requests.get(url)
    except exceptions.HTTPError as he:
        print("error: check the url", he)
        raise he
    except exceptions.ConnectionError as ce:
        print("error: check your connection", ce)
        raise ce

    try:
        data = request.json()
    except json.decoder.JSONDecodeError as je:
        print('error: could not convert request into json data', je)
        raise je

    return data

def main():
    response = call_api_for_search_term('blade')
    print(response)

if __name__ == '__main__':
    main()