#Sage 
#多项式
N =
p =
q =
Q.<x> = Zmod(q)[]
P.<y> = Zmod(p)[]

ex = 
hx = 

print('-------decrypt------')
qq = x^N-1
pp = y^N-1
hn = [int(x) for x in hx.coefficients()]
n = len(hn)
A1 = matrix.identity(n)
A0 = matrix.zero(n)
Aq = matrix.identity(n) * q
Ah = matrix(ZZ, [hn[-i:] + hn[:-i] for i in range(n)])
M = block_matrix([A1,Ah,A0,Aq],nrows=2)
L = M.LLL()
v = L[0]
f = list(v)[:n]
g = list(v)[n:]
fx = Q(f)
fy = P(f)
gx = Q(g)
Fqx = fx.inverse_mod(qq)
Fpy = fy.inverse_mod(pp)

#hxx = (Fqx*gx).mod(x^N-1)
#print(hxx==hx)

ax = (fx*ex).mod(qq)
an = [int(x) for x in ax.coefficients()]
#中心提升(centerlift)，使域范围从[0,q)变换到(-q/2,q/2)
for i in range(len(an)):
	if an[i] > q//2:
		an[i] -= q
ax = P(an)
print(ax)
out = (Fpy * ax).mod(pp)
print(out)

print(bytes(out.coefficients()))
