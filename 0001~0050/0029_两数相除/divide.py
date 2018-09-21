class Solution:
    def divide(self, dividend, divisor):
        rtn = 0
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            rtn = - (abs(dividend) // abs(divisor))
        else:
            rtn = dividend // divisor
        if rtn < -2**31 or rtn > 2**31 - 1:
            return 2**31 - 1
        return rtn