# 仿射密码对应字母表
def affine(a, b):
	for i in range(26):
		print (chr(i+65) + ": " + chr(((a*i+b)%26)+65))