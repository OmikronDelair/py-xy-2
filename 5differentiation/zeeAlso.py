#
# derivation
# 
# numpy.org/doc/stable/reference/routines.polynomials.html
#
# LEGACY
# numpy.org/doc/stable/reference/generated/numpy.poly1d.html
# numpy.org/doc/stable/reference/generated/numpy.polyder.html
#

from numpy.polynomial import Polynomial as P

p = P([1,2,3,4])
# 1 + 2x + 3x**2 + 4x**3
print(p)

# (d/dx)(c) = 2 + 6x + 12x**2
d = p.deriv(1)
print(d)

