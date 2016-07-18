import os

for i in range(5062, 5095):
	os.system('wget https://raw.githubusercontent.com/OpenTechSummit/2016.opentechsummit.net/gh-pages/programm/audio/%s.mp3'%i)
	