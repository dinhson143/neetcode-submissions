class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        temp = [-num for num in nums]
        heapq.heapify(temp)

        result = 0
        while k > 0:
            result = -heapq.heappop(temp)
            # print(result)
            k -= 1

        return result

        