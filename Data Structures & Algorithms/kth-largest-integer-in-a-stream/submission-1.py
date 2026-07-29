import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
       self.kth = k
       self.nums = nums
       heapq.heapify(self.nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        # print(sorted(self.nums))
        return sorted(self.nums)[-self.kth]
