class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        result = []
        for s in strs:
            see = "".join(sorted(list(s)))
            if see in seen.keys():
                seen[see].append(s)
            else:
                seen[see] = [s]
        
        for item in seen.values():
            if item is not None:
                result.append(item)
        return result