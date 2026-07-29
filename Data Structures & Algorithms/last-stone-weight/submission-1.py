class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)
        print(max_heap)

        while len(max_heap) > 1:
            stone1 = -heapq.heappop(max_heap)
            stone2 = -heapq.heappop(max_heap)

            if stone1 == stone2:
                continue
            elif stone1 > stone2:
                heapq.heappush(max_heap, -(stone1-stone2)) 
            else:
                heapq.heappush(max_heap, -(stone2-stone1)) 

            # print(max_heap)
        
        return -heapq.heappop(max_heap) if max_heap else 0


