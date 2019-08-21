class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        m = len(grid[0])
        myMap = [[0 for x in range(m + 2)] for y in range(n + 2)]
        for x in range(0, m):
            for y in range(0, n):
                myMap[y + 1][x + 1] = grid[y][x]

        seashore = 0
        for x in range(1, m + 1):
            for y in range(1, n + 1):
                if myMap[y][x]==1:
                    if myMap[y - 1][x] == 0:
                        seashore += 1
                    if myMap[y + 1][x] == 0:
                        seashore += 1
                    if myMap[y][x + 1] == 0:
                        seashore += 1
                    if myMap[y][x - 1] == 0:
                        seashore += 1
        return seashore

sln=Solution()
assert 16==sln.islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]])
