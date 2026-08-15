class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.result = {}
        nums.sort()

        def backtrack(index, current_composition):
            if str(current_composition) not in self.result.keys():
                # print(self.result)
                self.result[str(current_composition)] = list(current_composition)

            for i in range(index, len(nums)):
                current_composition.append(nums[i])
                backtrack(i + 1, current_composition)
                current_composition.pop()


        backtrack(0, [])
        return list(self.result.values())


