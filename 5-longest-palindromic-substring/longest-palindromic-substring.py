class Solution:
    def longestPalindrome(self, s: str) -> str:

        if(not s):
            return ""
        n = len(s)
        
        def expand_around_center(s, left, right): 
            while(left >= 0 and right < len(s) and s[left] == s[right]):
                left -= 1
                right += 1
            return right - left - 1

        start = 0
        end = 0

        for i in range(n):
            odd = expand_around_center(s, i, i)
            even = expand_around_center(s, i, i+1)
            max_len = max(odd, even)

            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + (max_len) // 2

        return s[start:end+1]


        # if len(s) % 2 == 1:
        #     left = (len(s)-1) // 2
        #     right =  len(s) // 2
        # else:
        #     left =  right = len(s) // 2

        # substrings = []


        # while(left > 0 and right < len(s)):
            
        #     substring = s[left:right]

        #     if substring == substring[::-1]:
        #         substrings.append(substring)

        #     left -= 1
        #     right += 1

        # return substring[-1]