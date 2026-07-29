class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1

        if len(nums) == 0:
            return 0

        start_index = 0
        last_index = 0
        max_len = 0
        nums_sorted = sorted(list(set(nums)))

        print(nums_sorted)

        for i in range(1, len(nums_sorted)):
            if nums_sorted[i] - nums_sorted[i-1] > 1:
                max_len = max(max_len, last_index - start_index + 1)
                print(last_index)
                print(start_index)
                start_index = i
            
            last_index = i

        max_len = max(max_len, last_index - start_index + 1)
        return max_len

