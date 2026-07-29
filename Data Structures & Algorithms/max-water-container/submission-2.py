class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_area = 0
        while left <= right:
            l_value = heights[left]
            r_value = heights[right]

            width = min(l_value, r_value)
            length = right - left
            max_area = max(width*length, max_area)

            if l_value < r_value:
                left += 1          
            elif r_value <= l_value:
                right -= 1        

        
        print(max_area)
        return max_area