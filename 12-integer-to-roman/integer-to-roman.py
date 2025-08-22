class Solution:
    def intToRoman(self, num: int) -> str:

        roman = {
            "ones" : ["","I","II","III","IV","V","VI","VII","VIII","IX"],
            "tens" : ["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"],
            "hundreds" : ["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"],
            "thousands" : ["","M","MM","MMM"]
        }

        ThousandDigit = num // 1000
        HundredDigit = (num // 100) % 10
        TenDigit = (num // 10) % 10
        OneDigit = num % 10

        thousand = roman["thousands"][ThousandDigit]
        hundred = roman["hundreds"][HundredDigit]
        ten = roman["tens"][TenDigit]
        one = roman["ones"][OneDigit]

        return thousand + hundred + ten + one
        

        


        