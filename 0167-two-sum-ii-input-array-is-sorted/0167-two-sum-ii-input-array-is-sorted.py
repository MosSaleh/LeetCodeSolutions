class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        numToIndex = {}

        for i, n in enumerate(numbers, start=1):
            complement = target - n
            
            if complement in numToIndex and numToIndex[complement] < i:
                return [numToIndex[complement], i] 
            
            numToIndex[n] = i
         
        