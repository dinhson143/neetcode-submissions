class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        seen = nums
        for i, num in enumerate(nums):
           filtered = [x for index, x in enumerate(seen) if index != i]
           
           if len(filtered) < 1:
            value = 0
           else:
            value = math.prod(filtered)

           output.append(value)
        
        return output