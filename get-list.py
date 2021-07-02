#!/usr/bin/python

import json
from operator import itemgetter
import requests


##########################
## VARIABLES
## -----------
## NOTE: you only need the key and secret if you want to pull items that require authentication (see README).
## In my case, I wanted the album image URLs.
##
##########################

usernames = ['USERNAME1', 'USERNAME2']
results = '1000'
key = 'YOUR_KEY'
secret = 'YOUR_SECRET'

combined_collection = []


for username in usernames:
    r = requests.get(url='https://api.discogs.com/users/{}/collection/folders/0/releases?callback=&sort=artist&sort_order=asc&per_page={}&key={}&secret={}'.format(username,results,key,secret))
    if r.status_code != 200:
        print ("Bad.") #use webhook to send alert?
    else:
        collection_list = r.json()['releases']
        for album in collection_list:
            collection_dict = {}
            collection_dict['title'] = album['basic_information']['title']
            collection_dict['issued'] = album['basic_information']['year']
            collection_dict['artist'] = album['basic_information']['artists'][0]['name']
            collection_dict['cover_url'] = album['basic_information']['cover_image']
            collection_dict['owner'] = username
            combined_collection.append(collection_dict)
        #log something like "Username collection retrieved."

sorted_combined_collection = sorted(combined_collection, key=itemgetter('artist', 'title'))

collection_file = open("record_collection.json","w")
#TO DO: add error handling

collection_file.write(json.dumps(sorted_combined_collection, indent=2))
#TO DO: log something like "Collection saved to file."

collection_file.close()

#print (combined_collection)
