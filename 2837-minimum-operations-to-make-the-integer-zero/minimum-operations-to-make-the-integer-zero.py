class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        for op in range(1, 61):
            rem = num1 - op * num2
            if rem < op:
                continue
            pop = bin(rem).count("1")
            if pop <= op <= rem:
                return op
        return -1