#dp ≡ d mod (p-1) ，dq ≡ d mod (q-1) ，m ≡ cd (mod n) ，n = p * q

import gmpy2 as gp
e = 123
n = gp.mpz()
dp = gp.mpz()
c = gp.mpz()

for x in range(1, e):
    if(e*dp%x==1):
        p=(e*dp-1)//x+1
        if(n%p!=0):
            continue
        q=n//p
        phin=(p-1)*(q-1)
        d=gp.invert(e, phin)
        m=gp.powmod(c, d, n)
        if(len(hex(m)[2:])%2==1):
            continue
        print('--------------')
        print(m)
        print(hex(m)[2:])
        print(bytes.fromhex(hex(m)[2:]))