class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        high = len(nums) - 1
        low = 0
        result = -1
        chk = list()
        for i in range(0, len(nums)):
            chk.append(False)
        while(True):
            if high < low:
                result = low
                break
            if high == low:
                result = low
                break
            mid = (high + low) // 2
            if chk[mid] == True:
                if nums[mid] > target:
                    result = mid
                else :
                    result = mid - 1
                break                
            else :
                chk[mid] = True
            print("mid = ", mid)
            if nums[mid] == target:
                result = mid
                break
            elif nums[mid] < target:
                low = mid
            elif nums[mid] > target:
                high = mid
        print(nums[result])
        return result