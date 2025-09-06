class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        difference = {}
        result = []

        for i, num in enumerate(nums):
            diff = target - num

            if diff in difference:
                result.append(difference[diff])
                result.append(i)

            difference[num] = i
            
        
        return result
        
        
       
                