# https://www.youtube.com/watch?v=HBahE5MO9uE


from z3 import Ints, Optimize, sat

x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, costs = Ints('x1 x2 x3 x4 x5 x6 x7 x8 x9 x10 x11 x12 x13 x14 costs')

s = Optimize()

costs = 9*x1 + 6*x2 + 4*x3 + 7*x4 + 6*x5 +5*x6 +6*x7 + 4*x8 + \
        8*x9 + 3*x10 + 9*x11 +4*x12 + 6*x13 +7*x14



s.add(x1+x2 <= 550)
s.add(x3+x4 <= 300)
s.add(x5+x6 <= 433)
s.add(x7+x11 == 100)
s.add(x8+x12 == 200)
s.add(x9+x13 == 180)
s.add(x10+x14 == 250)
s.add(x1+x3+x5 == x7+x8+x9+x10)
s.add(x2+x4+x6 == x11+x12+x13+x14)
s.add(x1>=0, x2>=0)
# s.add(x2>=0)
s.add(x3>=0)
s.add(x4>=0)
s.add(x5>=0)
s.add(x6>=0)
s.add(x7>=0)
s.add(x8>=0)
s.add(x9>=0)
s.add(x10>=0)
s.add(x11>=0)
s.add(x12>=0)
s.add(x13>=0)
s.add(x14>=0)


s.minimize(costs)

print(s.check())
if s.check() == sat:
    print(s.model())




