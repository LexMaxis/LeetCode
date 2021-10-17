class Solution(object):
    def reverse(self, x):
        UP = 2147483647
        DOWN = -2147483648
        temp = 0
        y = x
        y = abs(y)

        while y > 0:
            temp2 = y % 10
            y = int(y/10)
            temp = temp*10 + temp2

        # 边界值判断
        if temp > UP or temp < DOWN:
            return 0

        # 正负判断
        if x < 0:
            return -temp
        else:
            return temp