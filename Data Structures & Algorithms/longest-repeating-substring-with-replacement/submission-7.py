class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = l + k
        dem = 0
        arr = list(s)
        result = 0
        while l < len(arr):
            # print(arr[l:r])
            # print(m_freq)
            window = len(arr[l:r])
            m_freq = sorted(dict(Counter(arr[l:r+1])).items(), key = lambda x:x[1], reverse=True)[0][1]
            # print(m_freq)
            if r < len(arr) and window - m_freq < k:
                r += 1
                result = max(result, len(arr[l:r]))
                # print(arr[l:r])
            else:
                l += 1
                r = l + k

        return result
