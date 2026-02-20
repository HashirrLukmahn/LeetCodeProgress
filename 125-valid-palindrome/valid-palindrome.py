class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        chars = []

        alphanum = ""
        for char in s:
            if char.isalnum():
                chars.append(char)
    
        alphanum = "".join(chars)

        alphanum = alphanum.lower()
        left = 0
        right = len(alphanum)-1

        while(left <= right):

            if(alphanum[left] != alphanum[right]):
                return False

            left += 1
            right -= 1
        
        return True

        
        