class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:

        rows = len(matrix)
        cols = len(matrix[0])

        colMax = []
        for j in range(cols):
            colmax = float('-inf')
            for i in range(rows):
                element = matrix[i][j]
                colmax = max(colmax, element)
            colMax.append(colmax)


        rowMin = []
        for i in range(rows):
            rowmin = float('inf')
            for j in range(cols):
                element = matrix[i][j]
                rowmin = min(rowmin, element)
            rowMin.append(rowmin)
        
        luckyNumbers = []
        for i in range(rows):
            for j in range(cols):
                element = matrix[i][j]
                if element == rowMin[i] == colMax[j]:
                    luckyNumbers.append(element)

        return luckyNumbers
        
        