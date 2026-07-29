class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        r = 0
        result = ""

        while l < len(s):
            if s[l] not in t:
                l += 1
                r = l
                continue

            if Counter(t) - Counter(s[l:r+1]) == Counter():
                print(s[l:r+1])
                if result != "":
                    result = s[l:r+1] if len(result) > len(s[l:r+1]) else result
                else:
                    result = s[l:r+1]
                    
                l += 1
                r = l
                continue

            if r < len(s):
                r += 1
            else:
                l += 1
                r = l

        return result