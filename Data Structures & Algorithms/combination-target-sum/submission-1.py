class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.result = []

        def backtrack(index, current_composition, current_sum):
            if current_sum == target:
                # print(current_composition, current_sum)
                self.result.append(list(current_composition))
                return

            if index >= len(nums) or current_sum > target:
                return


            # Decision 1: select current
            current_composition.append(nums[index])

            backtrack(index, current_composition, current_sum+nums[index])

            # Decision 2: select continue num
            current_composition.pop()
            backtrack(index+1, current_composition, current_sum)

        backtrack(0, [], 0)
        return self.result




        