class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = -1
        for y in range(len(obstacleGrid)):
            if obstacleGrid[y][0] != -1:
                obstacleGrid[y][0] = 1
            else:
                break
        for y in range(len(obstacleGrid)):
            if obstacleGrid[0][y] != -1:
                obstacleGrid[0][y] = 1
            else:
                break
        for y in range(1, len(obstacleGrid)):
            for x in range(1, len(obstacleGrid[0])):
                if obstacleGrid[y-1][x] != -1:
                    obstacleGrid[y][x] += obstacleGrid[y-1][x]
                if obstacleGrid[y][x-1] != -1:
                    obstacleGrid[y][x] += obstacleGrid[y][x-1]
        return obstacleGrid[-1][-1]