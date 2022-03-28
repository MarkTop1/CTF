# Sage 
# Read ciphertext and public key.
c = []
c = vector(ZZ, c)

B = []
B = matrix(ZZ, B)

# Nguyen's Attack.
n = 150
delta = 3
s = vector(ZZ, [delta]*n)
B6 = B.change_ring(Zmod(2*delta))
left = (c + s).change_ring(Zmod(2*delta))
m6 = (B6.solve_left(left)).change_ring(ZZ)
new_c = (c - m6*B) * 2 / (2*delta)

# embedded technique
new_B = (B*2).stack(new_c).augment(vector(ZZ, [0]*n + [1]))
new_B = new_B.change_ring(ZZ)

new_B_BKZ = new_B.BKZ()
shortest_vector = new_B_BKZ[0]
mbar = (B*2).solve_left(new_c - shortest_vector[:-1])
m = mbar * (2*delta) + m6

print(bytes.fromhex(hex(m)[2:]))