class Solution:
    def isValid(self, s: str) -> bool:
        characters = {"(": ")", "{": "}", "[": "]"}
        seen = []
        arr = list(s)
        for c in arr:
            if c in set(characters.keys()):
                seen.append(c)
            else:
                if len(seen) == 0:
                    return False
                latest = seen.pop()
                if c != characters[latest]:
                    return False
        if len(seen) > 0:
            return False
        return True