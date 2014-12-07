#!/usr/bin/python3

import xml.dom.minidom, configparser, time
import urllib.request as ur
import hummingbird as hb

cf = configparser.ConfigParser()
cf.read('sayat.conf')

host = cf["plex"]["host"]
port = cf["plex"]["port"]

url = "http://"+host+":"+port+"/library/sections/1/recentlyViewed"
doc = xml.dom.minidom.parse(ur.urlopen(url))
attr = doc.getElementsByTagName("Video")[0].getAttribute("title")

def update_hb_lib():
	username = cf["hummingbird.me"]["user"]
	passw = cf["hummingbird.me"]["password"]
	hum = hb.Hummingbird(username, passw)
	bird = hum.get_library(username, status="currently-watching")

	titles = []
	for i in range(len(bird)):
  		titles.append(bird[i].anime.title.lower())

	plex_ep = int(attr.split(" - ")[1])
	ep_title = attr.split(" - ")[0]
	
	keyword = max(ep_title.split(" "), key=len).lower()

	for t in range(len(titles)):
		res = titles.index("".join([x for x in titles if keyword in x]))
		hb_id = bird[res].anime.anime_id
		ep_watched = bird[res].episodes_watched
		break
	
	print(ep_title, plex_ep)
	print(hb_id, ep_watched)

	if ep_watched < plex_ep:
		hum.update_entry(hb_id, episodes_watched=plex_ep)
		print("List updated.")

while True:
	update_hb_lib()
	time.sleep(5)