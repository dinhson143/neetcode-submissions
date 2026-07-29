class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        check = dict(Counter(nums))
        check = list(dict(sorted(check.items(), key=lambda item:item[1], reverse=True)).keys())

        return check[:k]