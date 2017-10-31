import json
import os
import io
import requests
from bs4 import BeautifulSoup as BS
try:
    to_unicode = unicode
except NameError:
    to_unicode = str
site = requests.get('https://developer.apple.com/wwdc/events/')
data = site.content.decode('utf-8')
Soup = BS(data, 'lxml')
path = "Apple WWDC/Data/Special Events"
if not os.path.exists(path):
    os.makedirs(path)
filename = 'Apple WWDC/Data/Special Events/evening_events_data.json'
with io.open(filename, 'w', encoding='utf8') as outfile:
    events = {'name': [], 'description': [], 'date-time': []}
    for ele in Soup.find_all('h2'):
        if ele.text != "\n\n":
            events['name'].append(ele.text)
    for ele in Soup.find_all('p', {'class': None}):
        events['description'].append(
            ele.text.replace("\t", "").replace("\n", ""))
    for ele in Soup.find_all('p', {'class': 'date-time'}):
        events['date-time'].append(
            ele.text.replace("\t", "").replace("\n", ""))

    str_ = json.dumps(events, indent=2, sort_keys=False,
                      separators=(',', ': '), ensure_ascii=False)
    outfile.write(to_unicode(str_))
