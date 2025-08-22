class Solution {
    public int romanToInt(String s) {
        
        HashMap<Character, Integer> dictionary = new HashMap<>();
        dictionary.put('I',1);
        dictionary.put('V',5);
        dictionary.put('X',10);
        dictionary.put('L',50);
        dictionary.put('C',100);
        dictionary.put('D',500);
        dictionary.put('M',1000);

        int result = 0;

        char[] roman = s.toCharArray();

        for(int i = 0; i < roman.length; i++){
            int currentval = dictionary.get(roman[i]);

            if(i+1 < roman.length && currentval < dictionary.get(roman[i+1])){
                result -= currentval;
            }
            else{
                result += currentval;
            }
        }

        return result;
    }
}