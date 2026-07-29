class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        result = min(nums[l], nums[r])
        while l <= r:
            m = (l+r) // 2
            result = min(result, nums[m])

            if nums[l] <= nums[m]:
                if nums[l] < result <= nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if nums[m] >= result >= nums[r]:
                    l = m + 1
                else:
                    r = m - 1

        return result