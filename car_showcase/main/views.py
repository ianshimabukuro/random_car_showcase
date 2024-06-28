import random

from django.shortcuts import render
import requests
import json
from bs4 import BeautifulSoup
from . import google_image_scraper
# Create your views here.

def showCars(request):

    page = random.randint(0,49)
    make = "honda"
    api_url = 'https://api.api-ninjas.com/v1/cars?limit=50&make={}'.format(make)
    response = requests.get(api_url, headers={'X-Api-Key': 'jFQIehzE63CSUj5jaggNLg==AiW7XrkI3zZvIsI6'})
    data = response.json()[page]


    query = data['make']+data['model']+str(data['year'])
    src = google_image_scraper.get_image_url(query)
    dict_image = {'src': src}
    data.update(dict_image)
    return render(request,'main/home.html',data)

