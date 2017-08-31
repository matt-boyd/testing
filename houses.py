#!/bin/bash

import feedparser

url = feedparser.parse('https://www.propertynews.com/rss.php?s=422487314')
for houses in url['items']:
	title =  houses['title'].encode('utf-8')
	link =  houses['link'].encode('utf-8')
	print title + "\n" +  link + "\n" + "\n" 



#This is a test.
