class Solution(object):
    def plusOne(self, digits):
        n = len(digits)

        flag = False

        if n == 1:
            if digits[0] == 9:
                return [1, 0]
            else:
                digits[0] += 1
                return digits

        else:
            if digits[n-1] + 1 == 10:
                flag = True
                digits[n-1] = 0
            else:
                digits[n-1] += 1

            for i in range(n - 2, -1, -1):
                if flag:
                    digits[i] += 1
                    if digits[i] == 10:
                        flag = True
                        digits[i] = 0
                    else:
                        flag = False

            if digits[0] == 0:
                digits[0] = 0
                digits.insert(0, 1)

        return digits