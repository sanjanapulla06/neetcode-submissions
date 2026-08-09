class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = sorted(stones)
        
        while len(stones) > 1:
            y = stones.pop()      # largest (last element after sorting)
            x = stones.pop()      # second largest
            
            if y != x:
                stones.append(y - x)
                stones.sort()
        
        return stones[0] if stones else 0