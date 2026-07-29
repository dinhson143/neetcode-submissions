class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = []
        i = 0
        j = 0
        while i < len(nums1) or j < len(nums2):
            if i < len(nums1) and j < len(nums2):
                if nums1[i] <= nums2[j]:
                    merged.append(nums1[i])
                    i += 1
                else:
                    merged.append(nums2[j])
                    j += 1
            elif i < len(nums1):
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1
        
        mid = len(merged) // 2
        result = []
        if len(merged[0:mid]) != len(merged[mid+1:len(merged)]):
            result = merged[mid-1:mid+1]
        else:
            result = [merged[mid]]
        print(merged)
        print(mid)
        print(merged[0:mid])
        print(merged[mid+1:len(merged)])
        print(result)
        return sum(result) / len(result)
            