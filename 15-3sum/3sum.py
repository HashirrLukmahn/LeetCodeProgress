class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 2:
            return []

        nums.sort()
        result = []
        

        for i in range(len(nums)):

            target = 0 - nums[i]
            if i > 0 and nums[i] == nums[i-1]:
                continue

            j = i + 1
            k = len(nums) - 1
            

            while(j < k):
                if nums[j] + nums[k] == target:
                    result.append([nums[i],nums[j],nums[k]])
                    while j < k and nums[j] == nums[j+1]:
                        j += 1
                    while j < k and nums[k] == nums[k-1]:
                        k -= 1
                    j += 1
                    k -= 1
                
                elif nums[j] + nums[k] < target:
                    j += 1

                elif nums[j] + nums[k] > target:
                    k -= 1

        return result
        
