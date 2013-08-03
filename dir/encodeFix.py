#!/usr/bin/python
# -*- coding: utf-8 -*-

# this script scans Kino no Journey ebooks or whatever that
# was unfortunately encoded in garbled shift-jis 
# and turn them into utf-8

import os
import codecs
import shutil


list1 = []
list2 = []

# this function grabs all directories in fname
# and put it in l

def fillList(l,fname):
	for dirname, dirnames, filenames in os.walk(fname):
		if dirname[0:3] == "./.":
			continue
		for subdirname in dirnames:
			l.append((os.path.join(dirname, subdirname))[len(fname):])

# this function grabs all filenames in fname, put in l

def fillNames(l,fname):
	for dirname, dirnames, filenames in os.walk(fname):
		if dirname[0:3] == "./.":
			continue
		for filename in filenames:
			l.append((os.path.join(dirname, filename))[len(fname):])

# these are the directories in question

a = "./(一般小説) [時雨沢恵一] キノの旅 第01巻～第09巻"
b = "./kino-fix"

fillList(list1,a)
fillNames(list2,a)

for i in list1:
	os.makedirs(b+i)


# errors will be stored here (shift-jis is wonky)
errors = []

for i in list2:
	# translate .txt files (which would be shit-jis normally) to .txt files of utf8
	if i[-3:] == "txt":
		f = codecs.open(a+i,mode="r",encoding='shift_jisx0212')
		g = codecs.open(b+i,mode="w",encoding='utf-8')
		line = 0
		while True:
			line+=1
			try:
				k = f.readline()	
				if k == "": break	
				g.write(k+"<br />")			
			except Exception:
				errors.append("line "+str(line)+": "+i)
	# just copy otherwise
	else:
		shutil.copy2(a+i,b+i)
		
# print errors
for i in set(errors):
	print i
