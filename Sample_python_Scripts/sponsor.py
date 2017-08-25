import urllib2
import json
site=urllib2.urlopen("https://us.pycon.org/2017/sponsors/")
from bs4 import BeautifulSoup
s=BeautifulSoup(site)
divs=s.find_all("div",{'class':'sponsor-level'})
spons=[]
for level in divs:
	levelname=level.find_all("h2")[0].string
	level_sponsors=level.find_all("div",{'class':'sponsor'})
	for level_sponsor in level_sponsors:
		anchor=level_sponsor.find_all("a")
		dictionary={}
		dictionary['id']=""
		dictionary['name']=anchor[1].string
		dictionary['level']=""
		dictionary['sponsor_Type']=levelname
		dictionary['url']=anchor[0]['href']
		dictionary['description']=level_sponsor.find_all("p")[1].string
		spons.append(dictionary)
sponsors_json=json.dumps(spons)
print sponsors_json