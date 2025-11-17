# nums와 k를 입력 받고
# 1과 1사이의 0 갯수가 k 보다 낮으면 False, 아니면 True

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        cnts = [0] * len(nums)
        minval = 987654321
        start = False
        for i in range(len(nums)):
            if not start and nums[i] == 1:
                start = True
                continue
            if start:
                if nums[i] == 0:
                    cnts[i] = cnts[i-1] + 1
                else:
                    print(cnts[i-1])
                    minval = min(minval, cnts[i-1])
                    if minval < k:
                        return False
        print(minval)
        print(cnts)
        return k <= minval