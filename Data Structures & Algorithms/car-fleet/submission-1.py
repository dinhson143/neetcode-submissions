class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = sorted(zip(position, speed), reverse=True)

        current_max_time = 0.0
        fleet = 0
        for p,s in arr:
            t = (target - p)/ s
            print(t)
            if t > current_max_time:
                fleet += 1
                current_max_time = t
            
        return fleet