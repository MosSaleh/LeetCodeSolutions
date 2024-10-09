class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        l, r = 0, len(numbers) -1

        while l < r:
            num = numbers[l] + numbers[r]

            if num < target:
                l += 1
            elif num > target:
                r -= 1
            else:
                return [l + 1, r + 1]
        
        return []
         
        