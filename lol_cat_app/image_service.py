import os
import requests
import shutil

access_key = 'L1H5FN4KisOgZOsmY7Q6-5JpxJq6De9AD3h8AJcqglg'

def get_image(dir, name):
    base_url = f'https://api.unsplash.com/photos/random?query={name}'
    id = f'&client_id={access_key}'

    data = call_api(base_url+id)
    raw = data['urls']['download']
    print(raw)
    #save_image(dir, name, data)

def save_image(dir, name, data):
    filename = os.path.join(dir, name + '.jpg')

    with open(filename, 'wb') as fout:
        shutil.copyfileobj(data, fout)

def call_api(url):
    response = requests.get(url, stream=True)
    return response.json()

def main():
    get_image('./cat-pictures', 'london')

if __name__ == '__main__':
    main()