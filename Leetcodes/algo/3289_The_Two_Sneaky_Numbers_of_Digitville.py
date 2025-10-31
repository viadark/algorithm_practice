from types import List

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        from collections import defaultdict
        d = defaultdict(int)
        for n in nums:
            d[n] += 1
        ret = []
        for k, v in d.items():
            if v >= 2:
                ret.append(k)
        return ret