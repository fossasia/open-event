import urllib2
import wget 
from bs4 import BeautifulSoup
url="https://us.pycon.org/2017/schedule/tutorials/list/"
tracks_page=urllib2.urlopen(url)
soup1=BeautifulSoup(tracks_page)
divs=soup1.find_all("div",{'class':'box-content'})
print divs
i=1
for div in divs:
	title=div.find_all("h2")
	for tag in title:
		session_url="https://us.pycon.org"+tag.find_all("a")[0]['href']
		session_page=urllib2.urlopen(session_url)
		soup2=BeautifulSoup(session_page)
		divtags=soup2.find_all("div",{'class':'box-content'})
		for divtag in divtags:
			speaker_url="https://us.pycon.org"+divtag.find_all("h4")[1].find_all("a")[0]['href']
			speaker_page=urllib2.urlopen(speaker_url)
			soup3=BeautifulSoup(speaker_page)
			image_box=soup3.find_all("div",{'class':'span2'})
			for images in image_box:
				try:
					x=images.find_all("img")[0]
				except IndexError:
					continue
				url=x['src']
				print url
				print i
				i=i+1
				downlink="https://us.pycon.org"+url
				wget.download(downlink)

