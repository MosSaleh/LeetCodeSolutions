class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = max(candies)
        ans = []
        for candy in candies:
            if candy + extraCandies >= maxCandies:
                ans.append(True)
            else:
                ans.append(False)
        return ans