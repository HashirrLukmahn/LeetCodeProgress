class Solution:
    def sumAndMultiply(self, n: int) -> int:

        if n == 0:
            return 0

        new_num = ""
        num = str(n)
        sum_nums = 0

        for digit in num:
            if digit != "0":
                new_num += digit
                sum_nums += int(digit)

        new_num_int = int(new_num)
        
        return new_num_int*sum_nums

        

        


        
        