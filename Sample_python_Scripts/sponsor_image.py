import urllib2
import wget
from bs4 import BeautifulSoup
site=urllib2.urlopen("https://us.pycon.org/2017/sponsors/")
page=BeautifulSoup(site)
divs=page.find_all("div",{'class':'sponsor'})
for div in divs:
	anchor=div.find_all("a")
	url=anchor[0].find_all("img")[0]['src']
	downlink="https://us.pycon.org"+url
	filename = wget.download(downlink)
	print filename