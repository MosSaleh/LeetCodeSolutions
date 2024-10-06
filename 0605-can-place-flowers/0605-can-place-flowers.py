class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbedcopy = [0] + flowerbed + [0]

        for i in range (1, len(flowerbedcopy) - 1):
            if not flowerbedcopy[i -1] and not flowerbedcopy[i+1] and not flowerbedcopy[i]:
                flowerbedcopy[i] = 1
                n -= 1
        
        return not n
            
