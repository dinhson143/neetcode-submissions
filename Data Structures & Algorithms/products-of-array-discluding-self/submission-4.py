class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        seen = nums
        for i, num in enumerate(nums):
            filtered = [x for index, x in enumerate(seen) if index != i]
            value = math.prod(filtered)

            output.append(value)
        
        return output