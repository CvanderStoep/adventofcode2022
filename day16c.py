import itertools

graph = {'AA': ['CC', 'BB'], 'BB': ['CC', 'AA', 'DD'], 'CC': ['AA', 'DD', 'BB'], 'DD': ['CC', 'BB']}
distances = {(v, l): 1 if l in graph[v] else 1000 for l in graph for v in graph}

distances[('AA', 'CC')] = 4
distances[('BB', 'DD')] = 5

# floyd-warshall = Distance for any possible pair of valves
for k, i, j in itertools.permutations(graph, 3):
    # print(f'{k= }, {i= }, {j= } ')
    distances[i, j] = min(distances[i, j], distances[i, k] + distances[k, j])
pass

print(distances[('AA', 'DD')])

# N = 4
# for subset in range(1 << N):
#     for k in range(N):
#         result = (1 << k) & subset
#         if result != 0:
#             print(f'the item at index {k= }  is in the current {subset= }')
#         else:
#             print(f'the item at index {k= }  is NOT in the current {subset= }')

