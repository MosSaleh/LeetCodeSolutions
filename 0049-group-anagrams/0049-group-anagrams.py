class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for i, string in enumerate(strs):
            sorted_string = ''.join(sorted(string))
            if sorted_string not in hashmap:
                hashmap[sorted_string] = []
            hashmap[sorted_string].append(i)

        ans = []
        for value in hashmap.values():
            lst = []
            for index in value:
                lst.append(strs[index])
            ans.append(lst)
        
        return ans


