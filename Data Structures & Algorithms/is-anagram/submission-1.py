class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_result = sorted(list(s))
        print(s_result)
        t_result = sorted(list(t))
        print(t_result)
        return s_result == t_result