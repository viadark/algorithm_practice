# You are given an array of integers nums and an integer k.
# Return the maximum sum of a subarray of nums, such that the size of the subarray is divisible by k.

# prefix sum을 먼저 구한 다음
# k의 수대로 windows 형태로 슬라이딩 하면서 i, i-k 의 합을 구한 배열을 하나 만들고
# 그 배열을 바탕으로 subarray 합의 최대값 구하는 dp를 적용하면 풀린다

class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        subsum = [0] * len(nums)
        subsum[0] = nums[0]
        dp = [0]*len(nums)
        for i in range(1, len(nums)):
            subsum[i] = subsum[i-1] + nums[i]
        #print(subsum)
        dp[k-1] = subsum[k-1]
        for i in range(k, len(nums)):
            dp[i] = subsum[i] - subsum[i-k]
        #print(dp)
        dp2 = [-987654321987654321] * len(nums)
        dp2[k-1] = dp[k-1]
        for i in range(k, len(nums)):
            dp2[i] = max(dp2[i-k] + dp[i], dp[i])
        #print(dp2)
        return max(dp2)