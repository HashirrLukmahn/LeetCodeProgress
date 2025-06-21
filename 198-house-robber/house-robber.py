class Solution:
    def rob(self, nums: List[int]) -> int:

        #Dynamic Programming

        n = len(nums)

        #Set Base Cases first

        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0],nums[1])

        #set up base cases for DP

        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])

        for i in range(2,n):
            #we either choose the current house and the next one or  skip the current jar
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])

        return dp[n-1]
        
        
        
        