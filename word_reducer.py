#!/usr/bin/env python

import sys
import re

wordcount = {}

for line in sys.stdin:
    line = line.strip()
    word, count = line.split('\t', 1)
    try:
        count = int(count)
    except ValueError:
        continue
 
    try:
        wordcount[word] = wordcount[word] + count
    except:
        wordcount[word] = count

angry = 0
sad = 0
happy_c = 0
weather = 0
for word in wordcount.keys():
    if word == "happy" or word == "cheerful" or word == "joyful" or word == "gleeful" or word == "delighted" or word == "smiling" or word =="cheery" or word == "merry" or word =="jovial" or word =="jolly" or word == "jocular" or word =="carefree" or word =="beaming" or word == "grinning" or word == "lighthearted" or word == "pleased" or word =="satisfied" or word =="gratified" or word =="thrilled" or word =="blissful":
	happy_c = happy_c + int(wordcount[word])
    if word == "sad" or word == "sorrow" or word == "unhappy" or word == "sorrowful" or word == "depressed" or word == "glum" or word == "heartbroken" or word == "dejected" or word  == "downcast" or word == "miserable" or word == "despondent" or word == "despairing" or word == "disconsolate" or word == "desolate" or word == "wretched" or word == "gloomy" or word == "dismal" or word =="melancholy" or word == "mournful": 
	sad = sad + int(wordcount[word])  
    if word == "angry" or word == "mad" or word == "annoyed" or word == "irritating" or word == "vexing" or word == "choleric" or word == "outraged" or word == "livid" or word  == "apoplectic" or word == "pissed": 
	angry = angry + int(wordcount[word])
    if word == "windy" or word == "snowy" or word == "raining" or word == "rainy" or word == "cloudy" or word == "sunny": 
	weather = weather + int(wordcount[word]) 
print "%d\t%d\t%d\t%d" % (angry, sad, happy_c, weather)
