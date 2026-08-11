class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(start_index: int, subset: list):
            result.append(list(subset))
            # print(result)

            for i in range(start_index, len(nums)):
                subset.append(nums[i])
                backtrack(i+1, subset)
                subset.pop()

        backtrack(0, [])
        return result