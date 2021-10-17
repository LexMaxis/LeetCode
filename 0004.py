class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        y = x
        sum = 0

        while y > 0:
            temp = y % 10
            y = int(y / 10)
            sum  = sum*10 + temp
        return x==sum

if __name__ == '__main__':
    s = Solution()
    s.isPalindrome(121)