class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)

        longestS = 0
        for num in hashset:
            if num - 1 in hashset:
                continue
            else:
                num += 1
                currS = 1
                while num in hashset:
                    currS += 1
                    num += 1
                if currS > longestS:
                    longestS = currS
                    
        return longestS