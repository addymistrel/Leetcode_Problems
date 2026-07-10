class Solution:
    def myAtoi(self, s: str) -> int:
        minVal, maxVal = (-1 * (2**31)), (2**31) - 1
        def round(x):
            if x < minVal:
                return minVal
            if x > maxVal:
                return maxVal
            return x
        s = s.strip()
        if len(s) == 0:
            return 0
        sign = -1 if s[0] == '-' else 1
        num = 0
        i = 0 if s[0] != '-' and s[0] != '+' else 1
        while i < len(s) and s == '0':
            i += 1
        while i < len(s):
            digit = ord(s[i]) - ord('0')
            if digit < 0 or digit > 9:
                break
            num = num * 10 + digit
            i += 1
        return round(sign * num)