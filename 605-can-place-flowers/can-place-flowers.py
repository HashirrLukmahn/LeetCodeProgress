class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        count = 0
        length =  len(flowerbed)
                

        for i in range(length):
            left_check = (i == 0) or (flowerbed[i-1] == 0)
            right_check = (i + 1 == length) or (flowerbed[i+1] == 0)

            if left_check and right_check and flowerbed[i] == 0:
                flowerbed[i] = 1
                count += 1

        return count >= n