class Solution:
    def reverseWords(self, s: str) -> str:

        #Strategy is to spilt words by spacing. We need to go char by char, create
        #a temp variable, the moment we find a space, we reset the word, and if there
        #consecutive spaces, we can just set the variable until we find our key word.
        wordStore = []
        result = ""

        wordStore = s.split()
        
        for word in reversed(wordStore):
            if word == " ":
                wordStore.pop(word)
            else:
                result += word + " "



        return result[:-1]

        