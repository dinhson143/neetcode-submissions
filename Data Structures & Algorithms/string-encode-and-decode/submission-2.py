class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) < 1:
            return "Null"
        encoded_string = "private_key".join(s for s in strs)
        return encoded_string



    def decode(self, s: str) -> List[str]:
        print(s)
        if s == "Null":
            return []
        decoded_strs = s.split("private_key")
        return decoded_strs
