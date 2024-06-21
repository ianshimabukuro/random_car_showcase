import random

from django.shortcuts import render
import requests
import json
from bs4 import BeautifulSoup
# Create your views here.

def showCars(request):

    page = random.randint(0,49)
    make = "audi"
    api_url = 'https://api.api-ninjas.com/v1/cars?limit=50&make={}'.format(make)
    response = requests.get(api_url, headers={'X-Api-Key': 'jFQIehzE63CSUj5jaggNLg==AiW7XrkI3zZvIsI6'})
    data = response.json()[page]

    word = "audi"
    url = 'https://www.google.com/search?q=audi&tbm=isch'
    content = requests.get(url).content
    soup = BeautifulSoup(content, 'lxml')
    image = soup.find('img',{"class": "YQ4gaf"})
    src = image.get('src')
    dict_image = {'image_src': src }
    data.update(dict_image)




    return render(request,'main/home.html',data)

