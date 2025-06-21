class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            value = nums[nums[i]]
            result.append(value)

        return result