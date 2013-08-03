s = "1 + 1"

def lex(string1,pos=0):
	point = ""
	result = []
	if pos >= len(string1):
		return []
	while '0' <= string1[pos] and string1[pos] <= '9':
		point += string1[pos]
		pos += 1
		if pos >= len(string1):
			break
	if point == "":
		if string1[pos] == ' ':
			return lex(string1,pos+1)
		else:
			return [string1[pos]] + lex(string1,pos+1)
	return [int(point)] + lex(string1,pos)

print lex(s)
funcs = {
	'+':lambda x,y: x+y,
	'-':lambda x,y: x-y,
	'*':lambda x,y: x*y,
	'/':lambda x,y: x/y}

class Refint:
	def __init__(self,val):
		self.val = val
	def add(self,num):
		self.val += num
		return self
def parseExp(lex1,pos):
	"e = (e) | n op e"
	if pos.val == len(lex1):
		return 0
	if type(lex1[pos.val]) == int:
		return funcs[lex1[pos.val+1]](lex1[pos.val], parseExp(lex1,pos.add(2)))
	elif lex1[pos.val] == '(':
		p = parseExp(lex1,pos.add(1))
		pos.add(1)
		return p
print parseExp(lex(s),Refint(0))
