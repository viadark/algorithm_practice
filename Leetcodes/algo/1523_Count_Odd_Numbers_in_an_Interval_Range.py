# 1523
# low ~ high (include) odd number 찾기

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high - low) // 2 + 1 if low % 2 != 0 or high % 2 != 0 else (high - low) // 2