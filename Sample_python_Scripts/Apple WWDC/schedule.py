import json
import os
import io
from selenium import webdriver
from bs4 import BeautifulSoup
try:
    to_unicode = unicode
except NameError:
    to_unicode = str


def clean_data(text):
    return text.replace("\t", "")


driver = webdriver.PhantomJS()
driver.set_window_size(1120, 520)
driver.get("https://developer.apple.com/wwdc/schedule/#/")
site = driver.page_source
data = site
soup = BeautifulSoup(data, 'lxml')
path = "Apple WWDC/Data/schedule/"

if not os.path.exists(path):
    os.makedirs(path)

day = soup.find_all("h4", {"class": "small-caps"})
title = soup.find_all("h4", {"class": "event-item-title"})
venue = soup.find_all("span", {"class": "event-item-byline block smaller"})

with io.open('Apple WWDC/Data/schedule/schedule_data.json',
             'w', encoding='utf8') as outfile:
    consultation = {"day": [], "title": [], "venue": []}
    for ele in title:
        consultation["title"].append(ele.text.strip())
    for ele in day:
        consultation["day"].append(ele.text.strip())
    for ele in venue:
        consultation["venue"].append(
            clean_data(ele.text.strip()).replace("\n", ", "))

    str_ = json.dumps(consultation, indent=2, sort_keys=False,
                      separators=(',', ': '), ensure_ascii=False)
    outfile.write(to_unicode(str_))
