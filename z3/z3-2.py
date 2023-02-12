# https://youtu.be/6F6hw_U-AX4


from z3 import *

x, y, z = Ints('x y z')

s2 = Solver()

s2.add(x > 1, x < 10)
s2.add(y > 1, y < 10)
s2.add(z > 1, y < 10)

s2.add(x**2 + y**2 == z**2)

print(s2.check())
if s2.check() == sat:
    print(s2.model())
