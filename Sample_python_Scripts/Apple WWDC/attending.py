import requests
import json
import os
import io
from bs4 import BeautifulSoup
try:
    to_unicode = unicode
except NameError:
    to_unicode = str


def clean_data(text):
    return text.replace("\t", "")


site = requests.get("https://developer.apple.com/wwdc/attending/")
data = site.content.decode('utf-8')
soup = BeautifulSoup(data, 'lxml')
path = "Apple WWDC/Data/Attending/"

if not os.path.exists(path):
    os.makedirs(path)

title = soup.find_all("h2", {"class": "typography-subsection-headline"})
topic = soup.find_all("strong")
description = soup.find_all("p", class_=lambda x:
                            x != ('typography-caption' and 'date-time'))[:-2]
time = soup.find_all("p", {"class": "date-time"})

with io.open('Apple WWDC/Data/Attending/attending_data.json',
             'w', encoding='utf8') as outfile:
    Attending = {"title": [], "topic": [],
                 "description": [], "time": []}
    for ele in title:
        Attending["title"].append(ele.text.strip())
    for ele in topic:
        Attending["topic"].append(ele.text.strip())
    for ele in description:
        Attending["description"].append(ele.text.strip().
                                        replace("\t", "").replace("\n", ""))
    for ele in time:
        Attending["time"].append(
            clean_data(ele.text.strip()).replace("\n", ", "))

    str_ = json.dumps(Attending, indent=2, sort_keys=False,
                      separators=(',', ': '), ensure_ascii=False)
    outfile.write(to_unicode(str_))
