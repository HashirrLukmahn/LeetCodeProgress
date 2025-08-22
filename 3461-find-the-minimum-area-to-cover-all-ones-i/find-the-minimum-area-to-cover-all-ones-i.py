class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        
        minCol = inf
        maxCol = -inf
        minRow = inf
        maxRow = -inf

        row = len(grid)
        col = len(grid[0])

        for i in range(row):
            for j in range(col):
                if (grid[i][j] == 1):
                    minRow = min(minRow,i)
                    minCol = min(minCol,j)
                    maxRow = max(maxRow,i)
                    maxCol = max(maxCol,j)

        return (maxRow-minRow + 1)  * (maxCol-minCol + 1)



        

        