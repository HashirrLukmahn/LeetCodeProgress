class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        lowest = math.inf
        mid = math.inf

        if n < 3:
            return False

        for i in range(n):
            lowest = min(nums[i],lowest)
            if nums[i] > lowest and nums[i] <= mid:
                mid = nums[i]

            if nums[i] > lowest and nums[i] > mid:
                return True

        return False



        
        