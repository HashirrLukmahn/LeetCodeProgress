class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:

        Firstdiff = abs(z - x)
        Secdiff = abs(z - y)
        
        if Firstdiff > Secdiff:
            return 2
        elif Secdiff > Firstdiff:
            return 1
        else:
            return 0