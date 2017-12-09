import os
import json
from bs4 import BeautifulSoup
import requests
import io
try:
    to_unicode = unicode
except NameError:
    to_unicode = str


def clean_data(text):
    return text.replace("\t", "")


site = requests.get('https://developer.apple.com/wwdc/get-togethers/')
data = site.content.decode('utf-8')
soup = BeautifulSoup(data, 'lxml')
title = soup.find_all(attrs={'class': 'typography-subsection-headline'})
description = soup.find_all('p', class_=lambda x: x != 'date-time')[1:]
locationAndTime = soup.find_all('p', attrs={'class': 'date-time'})

path = "Apple WWDC/Data/Get Together/"

if not os.path.exists(path):
    os.makedirs(path)

dictionary = {"title": [], "description": [], "location and time": []}
for x, y, z in zip(title, description, locationAndTime):
    dictionary["title"].append(x.text)
    dictionary["description"].append(clean_data(y.text))
    dictionary["location and time"].append(clean_data(z.text))
with io.open('Apple WWDC/Data/Get Together/get_togethers_data.json',
             'w', encoding='utf8') as outfile:
    str_ = json.dumps(dictionary, indent=2, sort_keys=False,
                      separators=(',', ': '), ensure_ascii=False)
    outfile.write(to_unicode(str_))
