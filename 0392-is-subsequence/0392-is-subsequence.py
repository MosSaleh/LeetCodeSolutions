class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        p_s, p_t = 0, 0

        while p_s < len(s) and p_t < len(t):
            if s[p_s] == t[p_t]:
                p_s += 1
            p_t += 1
        return p_s == len(s)