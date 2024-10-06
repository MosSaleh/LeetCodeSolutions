class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        length1, length2 = len(str1), len(str2)

        def isDivisor(l):
            if length1 % l or length2 % l:
                return False
            f1, f2 = length1 // l, length2 // l

            return str1[:l] * f1 == str1 and str1[:l] * f2 == str2

        for l in range(min(length1, length2), 0, -1):
            if isDivisor(l):
                return str1[:l]
        
        return ""

        