
def tostring(matrix):
	matrixprime = []
	for i in matrix:
		list1 = []
		for j in i:
			list1.append(str(j))
		matrixprime.append(list1)
	return matrixprime


def tolinearop(matrix, mul,source, dest):
	for i in range(len(matrix[dest])):
		if mul == 0 or matrix[source][i] == "0":
			pass
		elif matrix[dest][i][0] == "-":
			if (mul) == 1:
				matrix[dest][i] = matrix[source][i]+matrix[dest][i]
			else:
				matrix[dest][i] = str(mul)+"*("+matrix[source][i]+")"+matrix[dest][i]
		else:
			if (mul) == 1:
				matrix[dest][i] = matrix[source][i]+"+"+matrix[dest][i]
			else:
				matrix[dest][i] = str(mul)+"*("+matrix[source][i]+")"+"+"+matrix[dest][i]
	return matrix

def tosmop(matrix,mul,dest):
	for i in range(len(matrix[dest])):
		if mul == 0:
			pass
		else:
			matrix[dest][i] = str(mul)+"*("+matrix[dest][i]+")"
	return matrix

def top(matrix, palugit):
	for i in matrix:
		for j in i:
			s = j
			s += (palugit - len(s))*" "
			print s,
		print ""

print tostring([[-1,2,3],[0,-2,4]])
print tolinearop(tostring([[-1,2,3],[0,-2,4]]), 1,1,0)

def dotproduct(v1,v2):
	y = ""
	for i in range(len(v1)):
		y +=  v1[i][0]+"*"+v2[i][0]+"+"
	return y[:-1]

def tomato(v):
	y = []
	for i in range(len(v)):
		y.append( [str(v[i])] )
	return y
m = [
	["l-2",'0','4'],
	['5','l','-1'],
	['-7','0','l+1']
]

def scalar(sc,matrix):
	matrixprime = []
	for i in matrix:
		list1 = []
		for j in i:
			list1.append(str(sc)+"*"+"("+j+")")
		matrixprime.append(list1)
	return matrixprime
	
def add(m1,m2):
	for i in range(len(m1)):
		for j in range(len(m1[i])):
			if m1[i][j][0] == '-':
				m1[i][j] += m2[i][j]
			else:
				m1[i][j] += "+"+m2[i][j]
	return m1
	
def proj(u,v):
	return scalar("("+dotproduct(v,u)+"/"+dotproduct(u,u)+")",u)
def neg(m):
	return scalar("-1",m);
#print tolinearop(m,1,1,0)
top(m,14)
top(tolinearop(m,1,1,0),14)

top(
	scalar(
		dotproduct(
			tomato([1,2,3]),
			tomato([4,5,6])
		),
		[["1"]]
	),
	10
)

top(
	add(
		tomato([1,2,3]),
		tomato([1,2,3])
	),
	10
)

top(
	proj(
		neg([["u1"],["u2"],["u3"]]),
		[["v1"],["v2"],["v3"]]
	),
	10
)

top(tolinearop([['a','b','0','1'],['c','d','1','0']],"(c/a)",0,1),40)
top(tolinearop(tolinearop([['a','b','0','1'],['c','d','1','0']],  "(c/a)",0,1),  "(b/(c/a(b)+d))",1,0),40)
top(tolinearop(tolinearop(tolinearop([['a','b','0','1'],['c','d','1','0']],  "(c/a)",0,1),  "(b/(c/a(b)+d))",1,0), "(c/a(b)+d)",1,1),  40)
top(tosmop(
	tosmop(tolinearop(tolinearop([['a','b','0','1'],['c','d','1','0']],  "(c/a)",0,1),  "(b/(c/a(b)+d))",1,0), "(c/a(b)+d)",1),  "a",0),
40)


top(tosmop(
	tosmop(tolinearop(tolinearop([['2','3','0','1'],['5','7','1','0']],  "(5/2)",0,1),  "(3/(5/2)*(3)+7))",1,0), "((5/2)*(3)+2)",1),  "2",0),
40)
