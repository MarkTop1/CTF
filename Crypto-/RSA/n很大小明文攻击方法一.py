import binascii
import gmpy2
n=0xad03794ef170d81aad370dccb7b92af7d174c10e0ae9ddc99b7dc5f93af6c65b51cc9c40941b002c7633caf8cd50e1b73aa942c8488d46c0032064306de388151814982b6d35b4e2a62dd647f527b31b4f826c36848dc52999574a8694460e1b59b4e96bda1341d3ba5f991f0000a56004d47681ecfd37a5e64bd198617f8dad
e=0x3
c=0x10652cdf6f422470ea251f77

m=gmpy2.iroot(c, 3)[0]
print(binascii.unhexlify(hex(m)[2:].strip("L")))