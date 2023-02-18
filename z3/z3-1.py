"""
https://github.com/Antosser/mind-your-decisions-using-z3/blob/main/base_sum.py
"""


# https://youtu.be/ABj3IC9pYlQ

from z3 import Reals, sat, Solver

a, b, c, n= Reals('a b c n')

s = Solver()

s.add(a * 2 + b * 2 == 1)
s.add(a * 3 + c * 3 == 1)
s.add(b * 4 + c * 4 == 1)
s.add(a * n + b * n + c * n == 1)

print(s.check())
if s.check() == sat:
    print(s.model())


