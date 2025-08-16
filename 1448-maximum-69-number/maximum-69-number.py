class Solution:
    def maximum69Number (self, num: int) -> int:
        
        numString = str(num)

        for i in range(len(numString)):
            if numString[i] == '6':
                numString = numString.replace('6','9',1)
                break
        
        result = int(numString)

        return result

