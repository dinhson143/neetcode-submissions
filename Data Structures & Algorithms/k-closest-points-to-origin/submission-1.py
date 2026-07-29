class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        hpoints = []

        x = 0
        y = 0
        for point in points:
            d = (math.sqrt((point[0] - x)**2 + (point[1] - y)**2))
            hpoints.append([d, point])
        
        print(hpoints)
        heapq.heapify(hpoints)

        result = []
        for i in range(0, k):
            result.append(heapq.heappop(hpoints)[1])
        print(result)

        return result

