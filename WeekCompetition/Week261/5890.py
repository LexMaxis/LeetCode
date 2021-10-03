'''
给你一个字符串 s ，由 n 个字符组成，每个字符不是 'X' 就是 'O' 。

一次 操作 定义为从 s 中选出 三个连续字符 并将选中的每个字符都转换为 'O' 。注意，如果字符已经是 'O' ，只需要保持 不变 。

返回将 s 中所有字符均转换为 'O' 需要执行的 最少 操作次数
'''

class Solution(object):
    # 【myself】
    # def miniumMoves(self,s):
    #     n = len(s)
    #     i = 0
    #     j = 1
    #     k = 2
    #     count = 0
    #
    #     while k <= n:
    #         if s[i] =='X':
    #             if s[j] == 'X':
    #                 if s[k] == 'X':
    #                     i = k + 1
    #                     j = i + 1
    #                     k = i + 2
    #                     count += 1
    #                 else:
    #                     i = k
    #                     j = i + 1
    #                     k = i + 2
    #                     count += 1
    #             else:
    #                 if s[k] == 'X':
    #                     i = k + 1
    #                     j = i + 1
    #                     k = i + 2
    #                     count += 1
    #                 else:
    #                     i = k
    #                     j = i + 1
    #                     k = i + 2
    #                     count += 1
    #         else:
    #             if s[j] == 'X':
    #                 if s[k] == 'X':
    #                     i = k + 1
    #                     j = i + 1
    #                     k = i + 2
    #                     count += 1
    #                 else:
    #                     i = k
    #                     j = i + 1
    #                     k = i + 2
    #                     count += 1
    #             else:
    #                 if s[k] == 'X':
    #                     i = k + 1
    #                     j = i + 1
    #                     k = i + 2
    #                     count += 1
    #                 else:
    #                     i = k
    #                     j = i + 1
    #                     k = i + 2
    #                     count += 1

    #

    def miniumMoves(self, s):
        ans = 0
        n = len(s)
        l = 0
        while l < n:
            if s[l] == 'X':
                l += 3
                ans += 1
            else:
                 l += 1

        return ans

if __name__ == '__main__':
    s = Solution()
    str = "XXOOOOX"
    s.miniumMoves(str)