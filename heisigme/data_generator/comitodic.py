import json
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
	
print json.dumps(db)
