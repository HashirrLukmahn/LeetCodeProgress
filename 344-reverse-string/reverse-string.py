class Solution:
    def reverseString(self, s: List[str]) -> None:
        
        lo = 0
        hi = len(s) - 1

        while hi > lo:
            s[hi], s[lo] = s[lo], s[hi]
            hi -= 1
            lo += 1

