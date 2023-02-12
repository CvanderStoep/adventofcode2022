"""
from an array a[] of numbers, find the combinations that sum up to S
we use the bitwise operations to check all combination from 00000 to 11111
1<<n is a left bitwise shift (identical to 2^N)
"""


a = [3,1,2,4,7,2,1,5,4,1]
S = 27
n = len(a)
for mask in range(1<<n):
    sum = 0
    for i in range(n):
        if (mask & (1 << i)):
            sum += a[i]
    if sum == S:
        print('found', mask)