class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = [c.lower() for c in s if c.isalnum()]
        for i in range (len(string) // 2):
            if(string[i] != string[~i]):
                return False

        return True

        