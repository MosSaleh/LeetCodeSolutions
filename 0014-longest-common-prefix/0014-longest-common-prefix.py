class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        if not strs:
            return ""
        elif "" in strs:
            return ""
        else:
            word = strs[0]
        for i in range(len(word)):
            c = word[i]
            if (all(string[i] == c for string in strs)):
                prefix += c
            else:
                return prefix
    
            