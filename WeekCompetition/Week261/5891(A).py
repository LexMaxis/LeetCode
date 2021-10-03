'''
现有一份 n + m 次投掷单个 六面 骰子的观测数据，骰子的每个面从 1 到 6 编号。
观测数据中缺失了 n 份，你手上只拿到剩余 m 次投掷的数据。
幸好你有之前计算过的这 n + m 次投掷数据的 平均值 。
给你一个长度为 m 的整数数组 rolls ，
其中 rolls[i] 是第 i 次观测的值。同时给你两个整数 mean 和 n 。
返回一个长度为 n 的数组，包含所有缺失的观测数据，
且满足这 n + m 次投掷的 平均值 是 mean 。
如果存在多组符合要求的答案，只需要返回其中任意一组即可。如果不存在答案，返回一个空数组。
k 个数字的 平均值 为这些数字求和后再除以 k 。
注意 mean 是一个整数，所以 n + m 次投掷的总和需要被 n + m 整除。
'''


class Solution(object):
    def missingRolls(self, rolls, mean, n):
        m = len(rolls)
        sum_total = mean * (m + n)
        rolls_n = []

        sum_m = 0
        for i in range(0, m):
            sum_m += rolls[i]

        sum_n = sum_total - sum_m

        if sum_m + n * 6 < sum_total or sum_m >= sum_total or n > sum_n:
            return []

        else:
            temp = int(sum_n / n)

            for i in range(0, n):
                rolls_n.insert(i, temp)

        sum_temp = 0
        for i in range(0, n):
            sum_temp += rolls_n[i]

        if sum_temp < sum_n:
            rolls_n[0] += sum_n - sum_temp

        if rolls_n[0] > 6:

            for i in range(1, rolls_n[0] - 4):
                rolls_n[i] += 1

            rolls_n[0] = 5

        return rolls_n


if __name__ == '__main__':
    s = Solution()
    rolls = [4, 5, 6, 2, 3, 6, 5, 4, 6, 4, 5, 1, 6, 3, 1, 4, 5, 5, 3, 2, 3, 5, 3, 2, 1, 5, 4, 3, 5, 1, 5]
    s.missingRolls(rolls, 4, 40)
