import json
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream
import tweepy
from tweepy import OAuthHandler
from geopy.geocoders import Nominatim

from twitter import *

import sys
import csv

num_results = 480
max_range = 1

#Twitter for Authentication
twitter = Twitter(
		        auth = OAuth("1295392802-5LNsQozvWfuAEDCVmxGt5JQNgNUYqZB6DHeekvQ", "lHdN8PSTd9UvQllvboDEV6NyXrQF9jcF2xseY9P3oEeC2", "HEcBHrbQFyeCMOkHHsN05MgCT", "qLLjHgXdYw400Mz0m320FTw8wLC82tRX8EN7YAAlvkcBaHrKyp"))

#Creating CSV File
with open("Phila.txt","a") as csvfile:
	csvwriter = csv.writer(csvfile)

	geolocator = Nominatim()
	location = geolocator.geocode("Market Street Philadelphia")

	row = ["text","a"]
	csvwriter.writerow(row)

	result_count = 0
	last_id = None

	while result_count <  num_results:

	#Get all results and store in "query"
		query = twitter.search.tweets(q = "", geocode = "%f,%f,%dkm" % (float(location.latitude), float(location.longitude), max_range), count = 5, max_id = last_id)

	#Read results one by one
		for result in query["statuses"]:

			if result["geo"]:
				text = result["text"]
				text = text.encode('ascii', 'replace')

				row = [text]
				csvwriter.writerow(row)
				result_count += 1
			last_id = result["id"]								

		print "got %d results" % result_count

	csvfile.close()

	print "written to %s" % csvfile
