class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.result = []
        candidates.sort()

        def backtrack(i, current_composition, current_sum):
            # print(current_composition)
            if current_sum == target:
                self.result.append(list(current_composition))
                return

            if i >= len(candidates) or current_sum > target:
                return

            current_composition.append(candidates[i])
            backtrack(i+1, current_composition, current_sum + candidates[i])

            current_composition.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i+= 1

            backtrack(i+1, current_composition, current_sum)

        backtrack(0, [], 0)
        return self.result



        