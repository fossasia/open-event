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


site = requests.get("https://developer.apple.com/wwdc/consultations/")
data = site.content.decode('utf-8')
soup = BeautifulSoup(data, 'lxml')
path = "Apple WWDC/Data/Consultations/"

if not os.path.exists(path):
    os.makedirs(path)

title = soup.find_all("h2", {"class": "typography-subsection-headline"})
topic = soup.find_all("strong")[:-1]
time = soup.find_all("p", {"class": "date-time"})

with io.open('Apple WWDC/Data/Consultations/consultations_data.json',
             'w', encoding='utf8') as outfile:
    consultation = {"title": [], "topic": [],
                    "description": [], "time": []}
    for ele in title:
        consultation["title"].append(ele.text.strip())
    for ele in topic:
        consultation["topic"].append(ele.text.strip())
        consultation["description"].append(
            clean_data(ele.next_sibling.next_sibling).strip())
    consultation["description"].append(
        clean_data(title[-1].findNext("p").text.strip()))
    for ele in time:
        consultation["time"].append(
            clean_data(ele.text.strip()).replace("\n", ", "))

    str_ = json.dumps(consultation, indent=2, sort_keys=False,
                      separators=(',', ': '), ensure_ascii=False)
    outfile.write(to_unicode(str_))
