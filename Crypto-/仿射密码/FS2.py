import gmpy2
def affline_decode(cipher_text, a, b, m):
	plain_text = ''
	for i in cipher_text:
		if i in 'abcdefghijklmnopqrstuvwxyz':
			plain_text += chr(((ord(i)-ord('a'))-b)*gmpy2.invert(a,m) % m + ord('a'))
		else:
			plain_text += i
	print(plain_text)