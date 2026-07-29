class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        arr = [x for row in matrix for x in row]
        l = 0
        r = len(arr) - 1
        while l <= r:
            m = (l + r) // 2
            if arr[m] == target:
                return True

            elif arr[m] < target:
                l = m+1
            else:
                r = m-1

        return False