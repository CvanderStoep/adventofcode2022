# https://youtu.be/6F6hw_U-AX4


from z3 import Ints, Optimize, sat

x, y, z = Ints('x y z')

s = Optimize()


s.add(x - y == 1)
s.add(x > 1)
s.add(y > 1)
s.add(z > 1)
s.add(x < 10)
s.add(y < 10)
s.add(z < 10)

s.minimize(x)

print(s.check())
if s.check() == sat:
    print(s.model())




