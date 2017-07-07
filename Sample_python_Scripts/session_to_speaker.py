import json
f = open('x.txt', 'r')
js=f.read()
obj=json.loads(js)
speakers=[]
for o in obj:
	dictionary={}
	dictionary['id']=o['speakers'][0]['id']
	dictionary['name']=o['speakers'][0]['name']
	dictionary['email']=""
	dictionary['mobile']=""
	dictionary['photo']=""
	dictionary['organisation']=""
	dictionary['sessions']=[]
	dictionary['country']=""
	dictionary['short_biography']= ""
	dictionary['website']=""
	dictionary['twitter']=""
	dictionary['facebook']=""
	dictionary['github']=""
	dictionary["linkedin"]=""
	dictionary["position"]=""
	dictionary['city']=""
	dictionary['gender']=""
	dictionary['heard_from']=""
	dictionary['icon']=""
	dictionary['small']=""
	dictionary['speaking_experience']=""
	dictionary['sponsorship_required']=""
	dictionary['thumbnail']=""
	dictionary['featured']=""
	speakers.append(dictionary)
	speakers_json=json.dumps(speakers)
print speakers_json