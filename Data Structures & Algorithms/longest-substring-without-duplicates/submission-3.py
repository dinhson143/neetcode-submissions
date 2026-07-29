class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        seen = {}
        max_len = 0

        if len(s) == 1:
            return 1
        
        while r < len(s):
            if s[r] not in seen:
                seen[s[r]] = s[r]
                r += 1
            
            else:
                print(r)
                print(l)
                max_len = max(max_len, r - l)
                l += 1
                r = l + 1
                seen = {}
                seen[s[l]] = s[l]
        
        max_len = max(max_len, r - l)
        print(max_len)
        return max_len

