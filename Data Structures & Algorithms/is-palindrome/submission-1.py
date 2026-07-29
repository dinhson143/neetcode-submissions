class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr = list(s)
        origin = ""
        for char in s:
            char_lower = char.lower()
            if (char_lower >= 'a' and char_lower <= 'z') or (char_lower >= '0' and char_lower <= '9'):
                origin += char_lower

        print(origin)
        if origin == origin[::-1]:
            return True
        
        return False
        
