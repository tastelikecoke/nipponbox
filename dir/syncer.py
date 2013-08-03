#!/usr/bin/python
import os

list1 = []
list2 = []

# fill l with directories and filenames
def fillList(l,fname):
	for dirname, dirnames, filenames in os.walk(fname):
		if dirname[0:3] == "./.":
			continue
		if dirname.find(".wine") != -1:
			continue
		for subdirname in dirnames:
			l.append((os.path.join(dirname, subdirname))[len(fname):])
		for filename in filenames:
			if filename == "syncer_version":
				continue
			l.append((os.path.join(dirname, filename))[len(fname):])

# these two are to be searched for difference
a = "/home/kyon/Projects/Github/quanta/"
b = "/var/www/quanta/"
fillList(list1,a)
fillList(list2,b)

# print the differences!
for i in set(list1).difference(set(list2)):
	print a+i

for i in set(list2).difference(set(list1)):
	print b+i
