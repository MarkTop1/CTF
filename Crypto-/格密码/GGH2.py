# Sage
# e=mW+r
from sage.modules.free_module_integer import IntegerLattice

W = 
e = 

B = W.stack(e).augment(vector([0] * W.ncols() + [1]))
r = IntegerLattice(B).shortest_vector()
print('r = {}'.format(r))

m = W.solve_left(e - r[:-1])
print('m = {}'.format(m))
