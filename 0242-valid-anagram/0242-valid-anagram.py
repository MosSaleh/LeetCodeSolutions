class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False

        first_str = {}
        second_str = {}

        for char in s:
            first_str[char] = first_str.get(char,0) + 1

        for char in t:
            second_str[char] = second_str.get(char,0) + 1
        
        return first_str == second_str
        
        