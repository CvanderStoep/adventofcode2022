# set of Global variables; quite ugly, but works for now...
N = 6
dp = [[-1 for _ in range(N)] for _ in range(1 << N)]
dist = [[1000 for _ in range(N)] for _ in range(N)]

dist[0][1] = 5
dist[1][2] = 4
dist[0][4] = 1
dist[4][5] = 3
dist[2][5] = 2
dist[1][5] = 3
dist[3][4] = 1
dist[3][5] = 1
dist[2][3] = 1

for i in range(N):
    for j in range(N):
        if dist[i][j] < 1000:
            dist[j][i] = dist[i][j]


# The following function will calculate the shortest route that visits all unvisited
# cities in the bitmask starting from pos, and then goes back to the starting city

def solve(bitmask, pos):
    # If we have solved this subproblem previously, return the result that was recorded
    if dp[bitmask][pos] != -1:
        return dp[bitmask][pos]
    # If the bitmask is all 1s, we need to return home
    if bitmask == (1 << N) - 1:
        return dist[pos][0]
    # Keep track of the minimum distance we have seen when visiting other cities
    minDistance = 1000
    # For each city we haven't visited, we are going to try the subproblem that arises from visiting it
    for k in range(N):
        res = bitmask & (1 << k)
        # If we haven't visited the city before, try and visit it
        if res == 0:
            newBitmask = bitmask | (1 << k)
            # Get the distance from solving the subproblem
            newDist = dist[pos][k] + solve(newBitmask, k)
            # If newDist is smaller than the current minimum distance, we will override it here
            minDistance = min(minDistance, newDist)
    # Set the optimal value of the current subproblem
    dp[bitmask][pos] = minDistance
    return minDistance


if __name__ == '__main__':
    distance = solve(bitmask=1, pos=0)
    print(f'{distance= }')
