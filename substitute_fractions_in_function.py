## in the one i used fraction not number to get the result of the
## function a()

from fractions import Fraction

def a(x):
    b = 12*(x**3)
    c = -20*(x**2)
    d = 11*x
    return b+c+d-2

f = [Fraction(1,12),Fraction(1,6),Fraction(1,2),Fraction(1,4),
     Fraction(1,3),Fraction(-1,3),Fraction(-1,2),Fraction(-1,12),
     Fraction(-1,6),Fraction(-1,4),Fraction(2,3),Fraction(-2,3)]

for b in f:
    if a(b)==0:
        print b,a(b)

