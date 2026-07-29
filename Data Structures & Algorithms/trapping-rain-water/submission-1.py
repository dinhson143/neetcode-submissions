class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        l_max = height[l]
        r_max = height[r]
        total = 0

        while l < r:
            if height[l] < height[r]:
                l += 1
                # caculate
                l_max = max(l_max, height[l])
                total += l_max - height[l]
                print(f"left - {total}")
            else:
                r -= 1
                # caculate
                r_max = max(r_max, height[r])
                total += r_max - height[r]
                print(f"right - {total}")

        print(total)
        return total
