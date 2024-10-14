class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hashmap = {}

        for num in arr:
            hashmap[num] = hashmap.get(num, 0) + 1
        
        seen = set()
        for v in hashmap.values():
            if v in seen:
                return False
            seen.add(v)
        return True
