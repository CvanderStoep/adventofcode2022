# https://youtu.be/6F6hw_U-AX4


from z3 import Optimize, Reals, sat

x, y = Reals('x y')

s = Optimize()
# V = x**2 * y
# SA = 2 * x**2 + 4 * x * y

s.add(x > 3, x < 5)
s.add(y > 8, y < 15)
s.add(x**2 * y == 100)
s.minimize(2 * x**2 + 4 * x * y)

print(s.check())
if s.check() == sat:
    print(s.model())




