class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        head = 0
        tail = len(nums) - 1
        result = -1
        while True:
            center = (head + tail) // 2
            print("Center = ", center)
            temp = input()
            if tail == head:
                result = tail
                break
            if nums[center] == nums[center+1]:
                rightsize = tail - center + 1
                leftsize = center - head
                if rightsize % 2 == 0:
                    tail = center - 1
                    continue
                if leftsize % 2 == 0:
                    head = center
                    continue
            elif nums[center] == nums[center-1]:
                rightsize = tail - center
                leftsize = center - head + 1
                if rightsize % 2 == 0:
                    tail = center
                    continue
                if leftsize % 2 == 0:
                    head = center + 1
                    continue
            else:
                result = center
                break
        print("Res = ", result)

S = Solution()
print(S.singleNonDuplicate([1,1,2]))
