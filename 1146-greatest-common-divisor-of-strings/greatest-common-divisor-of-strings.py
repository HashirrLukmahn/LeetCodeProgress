class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        n = len(str2)
        m = len(str1)

        maxLength = min(m,n)

        for i in range(maxLength,0,-1):
            if m % i == 0 and n % i == 0: 
                candidate = str1[:i]  #this takes the length of the candidate based on the current index.

                if candidate * (m // len(candidate)) == str1 and candidate * (n // len(candidate)) == str2:
                    return candidate


        return ""