class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        result = 0
        for i in range(0, len(heights)):
            current_height = heights[i]
            for j in range(i, len(heights)):
                w = j+1 - i
                if heights[j] < current_height:
                    current_height = heights[j]
                result = max(result, w*current_height)
                
        return result