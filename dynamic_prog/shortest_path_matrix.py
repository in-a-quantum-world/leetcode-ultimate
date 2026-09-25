
#create an array dp which is 2d
# and represents the cheaopest copst to get from cell (i,j) tro the bvottom right corner (destination) itself

#given you can only move right or downwards in tyhis set up

#thje cheapest path from this cell to the end cell is the value in this cell itself, plus the cheapest route
#from either going down 1 (and then cheapest route from there)
#or going right 1 (and cheapest route from there)

#uses O(mn) time complex and O(mn) space omplex
def minpath(grid):
    m = len(grid) #how many rows there are
    n = len(grid[0]) # how many columns there are 

    dp = [[0]*n for _ in range(m)]  #cresates a 2d array with n zeroes per subarray, m subarrays

    for i in range(m-1,-1,-1): #starts at end, and traces back from there
        for j in range(n-1,-1,-1):
            if i == m-1 and j != n-1:
                dp[i][j] = grid[i][j] + dp[i][j+1]
            elif j == n-1 and i != m-1:
                dp[i][j] = grid[i][j] + dp[i+1][j]
            elif j == n-1 and i == m-1:
                dp[i][j] = grid[i][j]
            else:
                dp[i][j] = grid[i][j] + min(dp[i+1][j],dp[i][j+1])

    return dp[0][0]


#alternative solution with O(n) space complex instead!
#dyanmic prog 1d

#so dp(j) = grid(i,j) + min(dp(j),dp(j+1))

def minpath2(grid):
    m = len(grid)
    n = len(grid[0])

    dp = [0 for _ in range(len(grid[0]))] #grid of zeroes instead, matchhes number of columns 

    for i in range(m - 1,-1,-1):
        for j in range(n-1,-1,-1):
            if i == m-1 and j != n-1:
                dp[j] = grid[i][j] + dp[j+1]
            elif i != m-1 and j == n-1:
                dp[j] = grid[i][j] + dp[j]
            elif i != m-1 and j != n-1:
                dp[j] = grid[i][j] + min(dp[j], dp[j+1])

            else:
                dp[j] = grid[i][j] #column is updated to be equal to the last value (target value)

    return dp[0]

#well is it possible to do it in constant time instead?
#duhhhh

#just making changes to the grid matrix thing itself
def minpath3(grid):
    m = len(grid)
    n = len(grid[0])

    #just use the grid itself....

    for i in range(m-1,-1,-1):
        for j in range(n-1,-1,-1):
            if i == m-1 and j != n-1:
                grid[i][j] += grid[i][j+1]
            elif i != m-1 and j == n-1:
                grid[i][j] += grid[i+1][j]
            elif i != m-1 and j != n-1:
                grid[i][j] += min(grid[i][j+1],grid[i+1][j])

    

    return grid[0][0]