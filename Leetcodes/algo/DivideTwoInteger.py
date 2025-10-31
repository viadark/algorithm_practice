class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        isMinus = 1
        if dividend < 0:
            isMinus *= -1
            dividend = abs(dividend)
        if divisor < 0:
            isMinus *= -1
            divisor = abs(divisor)

        divtotal = 0
        divmultiplier = divisor
        cnt = 0
        cntmultiplier = 1
        while True:
            if divtotal + divisor > dividend:
                break
            if divtotal + divisor == dividend:
                cnt += 1
                break
            if divtotal + divmultiplier >= dividend:
                divmultiplier = divisor
                cntmultiplier = 1
                continue
            divtotal += divmultiplier
            divmultiplier += divmultiplier
            cnt += cntmultiplier
            cntmultiplier += cntmultiplier
            print("divtot = ", divtotal)
            print("cnt = ", cnt)
        cnt *= isMinus
        if cnt > 2147483647:
            cnt = 2147483647
        return cnt

s = Solution()
res = s.divide(-100, 3)
print("res = ", res)

        