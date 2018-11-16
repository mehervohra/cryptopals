from Crypto.Cipher import AES
import Challenge29
import Challenge215
import os
import random

def convertToDic(cookie):
	d = {}
	splitList = cookie.split("&")
	for elt in splitList:
		pair = elt.split("=")
		d[pair[0]] = pair[1]
	return d

def convertToCookie(d):
	s = ""
	s+="email=" + d["email"] + "&uid=" + str(d["uid"]) + "&role=" + d["role"]
	return s

def profile_for(email):
	d = {}
	rand_num = random.randint(0, 9)
	if ('=' in email or '&' in email):
		return ""
	d["email"] = email
	d["uid"] = rand_num
	d["role"] = "user"
	return convertToCookie(d)

#print(profile_for("foo@bar.com"))
#print(profile_for("foo@bar.com&role=admin"))

key = os.urandom(16)

def encrypt(email, BLOCKSIZE=16):
	ciph = AES.new(key, AES.MODE_ECB)
	padded = Challenge29.pkcsPadding(profile_for(email), BLOCKSIZE) 
	return ciph.encrypt(padded) 

# print(encrypt("foo@bar.com"))

def decrypt(userProfile, BLOCKSIZE=16):
    ciph = AES.new(key, AES.MODE_ECB)
    decrypted = ciph.decrypt(userProfile).decode()
    unpadded = Challenge215.validPKCS(decrypted, BLOCKSIZE)
    return unpadded

# print(decrypt(encrypt("foo@bar.com")))

def createAdmin(userProfile, BLOCKSIZE=16):
    ciph = AES.new(key, AES.MODE_ECB)
    encodedBlock = userProfile[:len(userProfile)-BLOCKSIZE]
    admin = ciph.encrypt(Challenge29.pkcsPadding(b'role=admin', BLOCKSIZE))
    return encodedBlock + admin

print(createAdmin(encrypt("foo@bar.com")))