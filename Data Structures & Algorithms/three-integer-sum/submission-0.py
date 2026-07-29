class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        for i in range(0, len(nums)):
            seen = {}
            num = nums[i]
            target = 0 - num
            for j in range(i+1, len(nums)):
                num_next = nums[j]
                if num_next in seen and sorted([num, seen[num_next], num_next]) not in result:
                    result.append(sorted([num, seen[num_next], num_next]))
                else:
                    seen[target-num_next] = num_next

        print(result)
        return result
