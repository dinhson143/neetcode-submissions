class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_result = sorted(list(s))
        t_result = sorted(list(t))
        return s_result == t_result