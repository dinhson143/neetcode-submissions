class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.result = []

        def backtrack(current_composition):
            # print(current_composition)
            if len(current_composition) == len(nums):
                self.result.append(list(current_composition))
                return

            if len(current_composition) > len(nums):
                return


            for num in nums:
                if num not in current_composition:
                    current_composition.append(num)
                    backtrack(current_composition)
                    current_composition.pop()

        backtrack([])

        return self.result

        