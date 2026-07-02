class Solution:
    def reverseVowels(self, s: str) -> str:

        vowels = {'a','e','i','o','u','A','E','I','O','U'}

        tracker = []
        word = []
        result = ""

        for char in s:
            if char in vowels:
                tracker.append(char)

            word.append(char)

        for i in range(len(word)):
            if word[i] in vowels:
                word[i] = tracker.pop()
            
            result += word[i]

        return result

        