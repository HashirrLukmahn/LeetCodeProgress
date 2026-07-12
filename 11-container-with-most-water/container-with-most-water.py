class Solution:
    def maxArea(self, height: List[int]) -> int:

        n =  len(height)
        left = 0
        right = n-1
        maxArea = 0

        while(left <= right):

            area = (right - left) * min(height[left],height[right])
            maxArea = max(maxArea,area)

            if height[left] > height[right]:
                right -= 1

            elif height[right] >= height[left]:
                left += 1

        return maxArea
        