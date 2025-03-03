
import requests
from requests.exceptions import ConnectionError



def get_image_url(url):
    try:
        response = requests.get(url)
        data = response.json()
        if data['status'] == 'error':
            print(f'Get error {data['message']}')
            return None
        return data['message']
    except ConnectionError:
        print('Error server')
        return None


def get_image(image_url: str):
    response = requests.get(image_url)
    return response.content


def download_image(image: bytes, name: str):
    with open(name, 'wb') as file:
        file.write(image)

N = 5
URL = 'https://dog.ceo/api/breeds/image/random'

for i in range(1, N+1):
    url = get_image_url(URL)
    print(url)
    image = get_image(image_url=url)
    name = f'dog.{i}.jpg'
    download_image(image, name)



