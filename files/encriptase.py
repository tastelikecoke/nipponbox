import getpass
# getting filename
print "filename>",
filename1 = raw_input()

defaultPassword = "os&aw3*GhsmB^&76bsnHcKNBnR^dj9*S"
# 32 char blocks.

# getting password
while True:
	password = getpass.getpass("password>")
	passwordConfirm = getpass.getpass("password(confirm)>")
	if passwordConfirm != password:
		print "not same! try again."
	else: break
while len(password) < 32:
	password += password
password = password[:32]
def sxor(s1,s2):
	return ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(s1,s2))

key1 = sxor(password,defaultPassword)

def encrypt(filename,key):
	file = open(filename,"rb")
	ivector = "8jsab2kj2svnow9YCHGbe3FejZxhBkf3"
	padding = "os&aw3*GhsmB^&76bsnHcKNBnR^dj9*S"
	cipher = ivector
	ciphertext = ""
	breakloop = True
	while breakloop:
		plaintext = file.read(32)
		if plaintext == "!:This is an encrypted file desu":
			file.close()
			decrypt(filename,key)
			return
		if len(plaintext) < 32:
			plaintext = plaintext + padding[len(plaintext):]
			breakloop = False
		cipher = sxor(sxor(plaintext,cipher),key)
		ciphertext += cipher
	file.close()
	file = open(filename,"wb")
	file.write("!:This is an encrypted file desu"+ciphertext)
		
	

def decrypt(filename,key):
	file = open(filename,"rb")
	file.read(32)
	ivector = "8jsab2kj2svnow9YCHGbe3FejZxhBkf3"
	padding = "os&aw3*GhsmB^&76bsnHcKNBnR^dj9*S"
	cipher = ivector
	plaintext = ""
	while True:
		cipherNew = file.read(32)
		if len(cipherNew) == 0: break
		plain = sxor(sxor(cipherNew,cipher),key)
		plaintext += plain
		cipher = cipherNew
	file.close()
	file = open(filename,"wb")
	file.write(plaintext)
	
encrypt(filename1,key1)