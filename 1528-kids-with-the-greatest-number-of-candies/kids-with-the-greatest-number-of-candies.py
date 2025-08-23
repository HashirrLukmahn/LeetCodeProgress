class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        LargestCandies = -inf
        result = []

        for i in range(len(candies)):
            LargestCandies = max(candies[i],LargestCandies)
        

        for i in range(len(candies)):
            if candies[i] + extraCandies >= LargestCandies:
                result.append(True)
            else:
                result.append(False)

        return result


