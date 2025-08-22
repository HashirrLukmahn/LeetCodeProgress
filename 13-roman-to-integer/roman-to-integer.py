class Solution:
    def romanToInt(self, s: str) -> int:

        roman = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }

        result = roman[s[0]]
        
        for i in range(1,len(s)):
            if roman[s[i]] <= roman[s[i-1]]:
                result += roman[s[i]]

            if roman[s[i]] > roman[s[i-1]]:
                result = result - (2 * roman[s[i-1]]) + roman[s[i]]

        return result
