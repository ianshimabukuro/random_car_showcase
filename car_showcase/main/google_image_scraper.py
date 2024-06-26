import requests
import json

import re



def get_image_url(query):

    API = 'AIzaSyDPqCUReJ4p83bxxxQBvRZitNA_vbHL9Bs'
    searchEngineID = 'c6fb1df3b10dd4278'
    url = 'https://www.googleapis.com/customsearch/v1?key=' + API + '&cx=' + searchEngineID + '&q=' + query +'&searchType=image&fileType=jpeg'

    response = requests.get(url)
    json = response.json()
    links = [item['link'] for item in json['items']]
    print(response.text)
    return links[0]

def Find(string):
    # findall() has been used
    # with valid conditions for urls in string
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex, string)
    return [x[0] for x in url]

src = get_image_url("audi a4 1996")
dict_image = src
print(src)