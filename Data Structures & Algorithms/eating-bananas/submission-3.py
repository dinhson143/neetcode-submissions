class Solution:
    def check(self, k: int, piles: List[int], hours: int) -> bool:
        h = 0
        for pile in piles:
            h += math.ceil(pile / k)

        print(f"K: {k} - Hours: {h}")
        return h <= hours

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        result = -1

        while l <= r:
            m = (l+r) // 2
            if self.check(m, piles, h) == True:
                result = min(m, result) if result > 0 else m
                r = m - 1        
            else:            
                l = m + 1  


        print(result)
        return result
                