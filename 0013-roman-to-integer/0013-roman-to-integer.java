class Solution {
    public int romanToInt(String s) {
        Map<String, Integer> romanMap = new HashMap<>();
        romanMap.put("I", 1);
        romanMap.put("V", 5);
        romanMap.put("X", 10);
        romanMap.put("L", 50);
        romanMap.put("C", 100);
        romanMap.put("D", 500);
        romanMap.put("M", 1000);

        romanMap.put("IV", 4);
        romanMap.put("IX", 9);
        romanMap.put("XL", 40);
        romanMap.put("XC", 90);
        romanMap.put("CD", 400);
        romanMap.put("CM", 900);

        int sum = 0;

        for (int i = 0; i < s.length(); i++) {
            if (i < s.length() - 1) {
                String exception = s.substring(i, i + 2);
                if (romanMap.containsKey(exception)) {
                    sum += romanMap.get(exception);
                    i++;
                    continue;
                }

            }
            sum += romanMap.get(String.valueOf(s.charAt(i)));

        }
        return sum;
    }

}