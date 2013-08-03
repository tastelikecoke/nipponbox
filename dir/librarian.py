#!/usr/bin/python
# it's a Librarian
# catalogs and compares directories
# Usage:
# librarian.py index                   -- index directory on dirversion
# librarian.py indexas [name]          -- index directory as [name]
# librarian.py compare [name1] [name2] -- compare directories
import os
import sys
import zlib

v = []
yesdot = False
nocompress = False

def getPathList(path):
	head = "null"
	list1 = []
	while head != "":
		head,path = os.path.split(path)
		list1.append(head)
	return list1


# fill l with directories and filenames
def fillList(l,fname):
	fname = os.path.join(fname,"")
	for dirname, dirnames, filenames in os.walk(fname):
		try:
			if dirname[len(fname)] == ".":
				if not yesdot: continue
		except IndexError:
			pass
		for subdirname in dirnames:
			if subdirname[0] == ".":
				if not yesdot: continue
			l.append(os.path.join(dirname, subdirname)[len(fname):])
		for filename in filenames:
			if filename[0] == ".":
				if not yesdot: continue
			if filename == "dirversion":
				continue
			l.append((os.path.join(dirname, filename))[len(fname):])

def fileToList(fname="./dirversion"):
	f = open(fname,"r")
	c = "null"
	list1 = []
	if nocompress:
		while c != "":
			c = f.readline()
			list1.append(c[:-1])
	else:
		c = f.read()
		c = zlib.decompress(c)
		list1 = c.splitlines()
	return list1

def makeList(a=".",fname="dirversion"):
	list1 = []
	fillList(list1,a)
	outname = os.path.join(a,fname)
	f = open(outname,"w")
	c = ""
	for i in list1:
		c += i+"\n"
	if nocompress:
		f.write(c)
	else: 
		f.write(zlib.compress(c))

def diffList(a,b):
	list1 = []
	list2 = []
	if os.path.isfile(a):
		#print "it's file."
		list1 = fileToList(fname=a)
	else:
		#print "it's not file."
		fillList(list1,a)
	#print "read", a
	
	if os.path.isfile(b):
		list2 = fileToList(fname=b)
	else: fillList(list2,b)
	#print "read", b
	
	# print the differences!
	count = 0
	for i in set(list1).difference(set(list2)):
		print os.path.join(a,i)
		count += 1
	for i in set(list2).difference(set(list1)):
		print os.path.join(b,i)
		count += 1
	
	if count == 0:
		print "no difference."
	else:
		print count, "differences."

for a in sys.argv:
	if a == "--yesdot":
		yesdot = True
	if a == "--nocompress":
		nocompress = True
	else:
		v.append(a)
		
if len(v) == 1:
	print "hi, I'm a librarian."
	print "--yesdot : includes dotted directories"
elif len(v) >= 2:
	if v[1] == "index":
		if len(v) == 2:
			makeList()
	elif v[1] == "indexas":
		if len(v) == 2:
			print "input a file name"
		else:
			makeList(fname=v[2])
	elif v[1] == "compare":
		if len(v) == 2:
			print "input a directory to compare."
		elif len(v) == 3:
			diffList(".",v[2])
		elif len(v) == 4:
			diffList(v[2],v[3])
