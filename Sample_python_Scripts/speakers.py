import urllib2
import json 
import os, urllib, sys
from bs4 import BeautifulSoup
from googleapiclient.discovery import build
url="https://us.pycon.org/2017/schedule/talks/list/"
tracks_page=urllib2.urlopen(url)
soup1=BeautifulSoup(tracks_page)
lists=[]
service = build("customsearch", "v1",
            developerKey="AIzaSyCbVul4dTty2c-1cd-sNPmaU5uwpe3fncc")
divs=soup1.find_all("div",{'class':'box-content'})
i=94
for div in divs:
	title=div.find_all("h2")[45:]
	for tag in title:
		dictionary={}
		dictionary['id']=i
		i=i+1
		session_url="https://us.pycon.org"+tag.find_all("a")[0]['href']
		session_name=tag.find_all("a")[0].string
		session_page=urllib2.urlopen(session_url)
		soup2=BeautifulSoup(session_page)
		divtags=soup2.find_all("div",{'class':'box-content'})
		for divtag in divtags:
			speaker_url="https://us.pycon.org"+divtag.find_all("h4")[1].find_all("a")[0]['href']
			dictionary['name']=divtag.find_all("h4")[1].find_all("a")[0].string
			dictionary['email']=""
			dictionary['mobile']=""
			dictionary['photo']="/images/speakers/.jpg"
			dictionary['organisation']=""
			dictionary['sessions']=[]
			sess={}
			sess['id']=""
			sess['title']=session_name
			dictionary['sessions'].append(sess)
			dictionary['country']=""
			dictionary['website']=""
			res_twitter = service.cse().list(q=str(dictionary['name'].encode('utf-8')),cx='009109434727877743699:odono8g0pmw',).execute()
			try:
				results_twitter=res_twitter['items'][0]['link']
			except KeyError:
				results_twitter=""
			dictionary['twitter']=results_twitter
			res_linked = service.cse().list(q=str(dictionary['name'].encode('utf-8')),cx='009109434727877743699:txk_d2noerw',).execute()
			try:
				results_linked=res_linked['items'][0]['link']
			except KeyError:
				results_linked=""
			dictionary['linkedin']=results_linked
			dictionary['position']=""
			dictionary['city']=""
			dictionary['heard_from']=""
			dictionary['icon']=""
			dictionary['small']=""
			dictionary['speaking_experience']=""
			dictionary['sponsorship_required']=""
			dictionary['thumbnail']=""
			dictionary['featured']=""
			speaker_page=urllib2.urlopen(speaker_url)
			soup3=BeautifulSoup(speaker_page)
			bio=soup3.find_all("div",{'class':'bio'})
			dictionary['short_biography']=""
			for para in bio:
				dictionary['short_biography']=dictionary['short_biography']+para.string
			dictionary['short_biography']= unicode(dictionary['short_biography']).replace("\r", '').replace("\n", '').replace("\t", '').replace("\"", '')	
			if " she " in str(dictionary['short_biography'].encode('utf-8')) or  " her " in str(dictionary['short_biography'].encode('utf-8')):
				dictionary['gender']="female"
			else: dictionary['gender']="male"
		lists.append(dictionary)
		print (dictionary)

print (json.dumps(lists))
