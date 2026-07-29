class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        arr = list(s2)
        arr1 = list(s1)

        l = 0
        r = 0
        while l < len(arr):
            if len(arr1) > 0 and r < len(arr) and arr[r] in arr1:
                arr1.remove(arr[r])
                r += 1
            else:
                # print(f"{arr[l:r]} - {len(arr[l:r])} - {len(s1)}")
                if len(arr[l:r]) == len(s1) and len(arr1) < 1:
                    return True
                l += 1
                r = l
                arr1 = list(s1)

        return False
        
        
                
            