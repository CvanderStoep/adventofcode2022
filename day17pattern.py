
def find_pattern(data: list[int]) -> tuple[list[int], list[int]]:
    for p in range(len(data)):
        sd = data[p:]
        for r in range(2, len(sd) // 2):
            if sd[0:r] == sd[r:2 * r]:
                if all([(sd[0:r] == sd[y:y + r]) for y in range(r, len(sd) - r, r)]):
                    return data[:p], data[p:p + r]
    return [], []

a = [1,3,4,3,4,3,3,4,5,3,4,5,3,4,5]

preamble, repetition = find_pattern(a)
print(preamble)
print(repetition)


