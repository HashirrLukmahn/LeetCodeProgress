class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
    
        binValue = []
        result = 0

        for i in range(32):
            if n % 2 == 0:
                binValue.append(0)
                n = n // 2
            elif n % 2 == 1:
                binValue.append(1)
                n = n // 2

        # for i in range(n//2):
        #      binValue[i],binValue[31-i] = binValue[31-i],binValue[i]

        for i in range(0,32):
            result += (binValue[i])*(2**(31-i))

        return result

        