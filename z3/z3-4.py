# https://youtu.be/6F6hw_U-AX4


from z3 import Optimize, Reals, sat

h, R, A, I = Reals('h R A I')

s = Optimize()
pi = 3.1415
A = 2 * pi * R * h + 2 * pi * R*R
I = h * pi * R*R

s.add(h > 0)
s.add(R > 0)

s.add(I == 1)
s.minimize(R)

print(s.check())
if s.check() == sat:
    print(s.model())




