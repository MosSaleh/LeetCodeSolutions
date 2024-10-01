class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = [c.lower() for c in s if c.isalnum()]

        return all(string[i] == string[~i] for i in range (len(string) // 2))

        