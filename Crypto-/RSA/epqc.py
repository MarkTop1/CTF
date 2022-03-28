import libnum
import gmpy2
import binascii

p=320181056072095218868339092717483179171
q=264515818482660146971535304176490802643
e=65537
c=21698323120385586424573862118808098555103084743518277473544693629498197679429
n = p * q
# print(n)
pai = (p-1)*(q-1)
d = gmpy2.invert(e,pai)
m = pow(c,d,n)

print(m)
# print(libnum.n2s(int(m)))
# print(binascii.a2b_hex(hex(int(m)).replace("0x","")))