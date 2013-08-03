#!/usr/bin/python
# coding:utf-8
from difflib import *
from subprocess import Popen, PIPE

f = open("Nya2.csv","r")
db = {}
for i in xrange(2042):
	s = f.readline().split("\t")
	db[s[1]] = s[0]
f.close()

f = open("ExtraNya.csv","r")
for i in xrange(4):
	s = f.readline().split("\t")
	db[s[1]] = s[0]
f.close()

f = open("Kana.csv","r")
for i in xrange(240):
	s = f.readline().split("\t")
	db[s[0]] = s[1]


while True:
	outs = ""
	input1 = raw_input()
	list1 = input1.split(",")
	isOutputNotExact = False
	for i in list1:
		try:
			outs += db[i]
		except KeyError:
			matches = get_close_matches(i,db.keys())
			if matches != []:
				isOutputNotExact = True
				outs += db[matches[0]]
			else: outs += "?"
		if outs[-1] == '\n':
			outs = outs[:-1]
	if isOutputNotExact: print "~",
	print outs
	p = Popen(['xsel','-b'], stdin=PIPE)
	p.communicate(input=outs)
