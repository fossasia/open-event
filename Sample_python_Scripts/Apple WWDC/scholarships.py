import json
import os
import io
import re
import requests
from bs4 import BeautifulSoup as BS

try:
    to_unicode = unicode
except NameError:
    to_unicode = str
site = requests.get('https://developer.apple.com/wwdc/scholarships/')
data = site.content.decode('utf-8')
Soup = BS(data, 'lxml')
path = os.path.join(os.getcwd(), "Data/Scholarships/")
if not os.path.exists(path):
    os.makedirs(path)
with io.open(os.path.join(os.getcwd(), "Data/Scholarships/scholarships.json"),
             'w', encoding='utf8') as outfile:
    scholarships = {}

    for ele in Soup.find_all('h2',
                             {'class': re.compile(
                                 "typography-section-headline [a-z,A-Z]*")}):
        scholarships[ele.string] = []
        nextNode = ele
        while nextNode is not None:
            nextNode = nextNode.nextSibling
            if nextNode is None:
                break
            if nextNode.string is None and nextNode.text is not None:
                string = nextNode.text.replace("\t", "").replace("\n", "")
                if len(string) != 0:
                    scholarships[ele.string].append(string)
            else:
                string = nextNode.string.replace("\t", "").replace("\n", "")
                if len(string) != 0:
                    scholarships[ele.string].append(string)

    for ele in Soup.find_all('h4',
                             {'class': re.compile(
                                 "typography-subsection-headline [a-z,A-Z]*")}):
        scholarships[ele.string] = []
        nextNode = ele
        while nextNode is not None:
            nextNode = nextNode.nextSibling
            if nextNode is None:
                break
            try:
                tag_name = nextNode.name
            except AttributeError:
                tag_name = ""
            if tag_name != "h4" and tag_name is not None:
                if tag_name == "ul":
                    scholarships[ele.string].extend(
                        filter(lambda x: len(x) > 0,
                               nextNode.text.split('\n')))
                if nextNode.string is None and nextNode.text is not None:
                    scholarships[ele.string]\
                        .append(nextNode.text.replace("\t", "")
                                .replace("\n", ""))
                else:
                    scholarships[ele.string]\
                        .append(nextNode.string.replace("\t", "")
                                .replace("\n", ""))
            elif tag_name == "h4":
                break

    scholarships['Deadline'] = []
    for ele in Soup.find_all('p', {'class': 'typography-caption'}):
        if ele.string is None and ele.text is not None:
            string = ele.text.replace("\t", "").replace("\n", "")
            if len(string) != 0:
                scholarships['Deadline'].append(string)
        else:
            string = ele.string.replace("\t", "").replace("\n", "")
            if len(string) != 0:
                scholarships['Deadline'].append(string)

    str_ = json.dumps(scholarships, indent=2, sort_keys=False,
                      separators=(',', ': '), ensure_ascii=False)
    outfile.write(to_unicode(str_))
