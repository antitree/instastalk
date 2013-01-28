#!/usr/bin/python
# Author: Antitree
# Description: Stalk your friends on Instagram. yay. 
# 1/27/2013

import json, urllib2, sys

if not len(sys.argv) == 3 :
  print("./instastalk.py (instagramID) (APItoken)")
  print("Find an instagram ID using this: http://jelled.com/instagram/lookup-user-id")
  sys.exit()

token = sys.argv[2]
users = [sys.argv[1]]


for user in users:
    #download json user information
    try:
      url = "https://api.instagram.com/v1/users/%s/media/recent/?access_token=%s" % (user, token)
      userjson = json.load(urllib2.urlopen(url))
    except:
      print("Couldn't download the URL",  sys.exc_info()[0], )
      print(url)
      continue

    locations = set([])  ##TODO: why am I doing it this way?

    try:
      for item  in userjson["data"]:
        #Extract locations
	if not item["location"] == None:
	    latitude = longitude = address = name = ""
            latitude = item["location"]["latitude"]
	    longitude = item["location"]["longitude"]
	    if "street_address" in item["location"]:
     	      address = item["location"]["street_address"]
	    if "name" in item["location"]:
	      name = item["location"]["name"]
            mapurl = "http://maps.google.com/maps?q=%s,+%s&iwloc=A&hl=en" % (latitude, longitude)

	    locations.add("Lat/Long:%s:%s \n Address: %s \nName: %s\nMap: %s" % (latitude, longitude, address, name, mapurl))
    except:
      print("ouch, Shit happens.", sys.exc_info()) 
      continue

    for l in locations:
      print(l)

