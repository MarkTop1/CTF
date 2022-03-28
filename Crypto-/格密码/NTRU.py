#Sage
h = 
p = 
c = 

v1 = vector(ZZ, [1, h])
v2 = vector(ZZ, [0, p])
m = matrix([v1,v2]);
f, g = m.LLL()[0]
print(f, g)

a = f*c % p % g
m = a * inverse_mod(f, g) % g
print(bytes.fromhex(hex(m)[2:]))

#利用这个网站跑https://sagecell.sagemath.org/

