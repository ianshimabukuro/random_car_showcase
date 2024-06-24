import requests
import json
def get_image_url(query):
    API = 'AIzaSyCLr1MvhuAUFcc3Hj34G2QtsRQFVJ6pmYg'
    searchEngineID = '15db288caa7c647bf'
    query = 'audi'
    url = 'https://www.googleapis.com/customsearch/v1?key=' + API + '&cx=' + searchEngineID + '&q=' + query

    response = requests.get(url)
    dict = json.loads(response.content)
    searchresults = dict['items']
    first = searchresults[0]
    second = first['pagemap']
    third = second['cse_image']
    return third[0]

