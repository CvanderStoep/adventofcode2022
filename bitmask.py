nums = [1, 2, 3, 4]
n = len(nums)
subsets = []
for mask in range(1 << n): #range(2 ** n):
    subset = []
    for i in range(n):
        if mask & (1 << i):
            subset.append(nums[i])
    subsets.append(subset[:])

print(f'{subsets= }')