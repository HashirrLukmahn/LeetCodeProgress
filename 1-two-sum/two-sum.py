class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        """ 
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            sum = nums[left] + nums[right]
            
            if sum == target:
                return [left, right]
            
            if sum < target:
                left += 1
            
            if sum > target:
                right -= 1
                
            
        
        return
        """
        
        difference = {}
        result = []

        for i, num in enumerate(nums):
            diff = target - num

            if diff in difference:
                result.append(difference[diff])
                result.append(i)

            difference[num] = i
            
        
        return result
        
        
       
                