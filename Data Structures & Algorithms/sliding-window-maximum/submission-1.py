class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        r = l + k
        result = []
        while l + k <= len(nums):
            # print(nums[l:r])
            result.append(max(nums[l:r]))
            l += 1
            r = l + k
        return result