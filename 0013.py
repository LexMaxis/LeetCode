class Solution(object):
    def romanToInt(self, s):
        Sum = 0
        number_single = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        for i in range(len(s) - 1):

            if number_single[s[i]] < number_single[s[i+1]]:
                Sum -= number_single[s[i]]
            else:
                Sum += number_single[s[i]]

        return Sum + number_single[s[-1]]