class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        l = 0
        r = l
        stack = []
        while l < len(temperatures):
            # print(stack)
            if r < len(temperatures) and temperatures[r] <= temperatures[l]:
                r += 1
            elif r < len(temperatures) and temperatures[r] > temperatures[l]:
                temp = r - l 
                stack.append(temp)
                l += 1
                r = l
            else:
                stack.append(0)
                l += 1
                r = l

        return stack
