class Solution(object):
    def getBorderLeft(self, nums, target, low, high):
        mid = (low + high) // 2
        res = 0
        if nums[low] == target:
            return low
        if nums[low+1] == target:
            return low+1
        if nums[mid] == target:
            res = self.getBorderLeft(nums, target, low, mid)
        else:
            res = self.getBorderLeft(nums, target, mid, high)
        return res
        
    def getBorderRight(self, nums, target, low, high):
        mid = (low + high) // 2
        res = 0
        if nums[high] == target:
            return high
        if nums[high-1] == target:
            return high-1
        if nums[mid] == target:
            res = self.getBorderRight(nums, target, mid, high)
        else:
            res = self.getBorderRight(nums, target, low, mid)
        return res

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return [-1, -1]
        low = 0
        high = len(nums)-1
        res = -1
        while True:
            if low > high:
                break
            mid = (low + high) // 2
            if nums[mid] == target:
                res = mid
                break
            if nums[mid] > target:
                high = mid - 1
            if nums[mid] < target:
                low = mid + 1
        if res == -1:
            return [-1, -1]
        start = self.getBorderLeft(nums, target, 0, res)
        end = self.getBorderRight(nums, target, res, len(nums)-1)
        return [start , end]

s = Solution()
res = s.searchRange([5, 7, 7, 8, 8, 10, 11, 12, 13, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 19], 17)
print("res = ", res)