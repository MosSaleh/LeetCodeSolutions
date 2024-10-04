class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}

        for num in nums:
            if num not in hashmap:
                hashmap[num] = 1
            else:
                hashmap[num] = hashmap.get(num) + 1
        
        sorted_values = list(sorted(hashmap.values()))
        ans = []
        added = set()
        
        while len(ans) < k:
            for key, value in hashmap.items():
                if value == sorted_values[-1] and key not in added:
                    ans.append(key)
                    added.add(key)
                    sorted_values.pop(-1)
                    break

        return ans
                


        
        