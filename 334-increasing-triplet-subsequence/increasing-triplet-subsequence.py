class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        lowest = math.inf
        mid = math.inf

        if n < 3:
            return False

        for i in range(n):
            
            if nums[i] <= lowest:
                lowest = nums[i]            
            elif nums[i] > lowest and nums[i] > mid:
                return True
            else:
                mid = nums[i]

        return False



        
        