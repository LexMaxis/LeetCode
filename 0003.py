'''
给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度
'''

class Solution(object):
    # def lengthOfLongestSubstring(self, s):
    #     # if len(s) == 0:
    #     #     return 0
    #
    #     if s == '""':
    #         return 0
    #
    #     container_1 = []
    #     container_2 = []
    #     container_2.insert(0, s[0])
    #     for i in range(1, len(s)):
    #         j = i
    #         while s[j] not in container_1:
    #             container_2.append(s[i])
    #             j += 1
    #
    #         if len(container_1) < len(container_2):
    #             container_1 = container_2
    #             container_2 = []
    #
    #     return len(container_1)

    def lengthOfLongestSubstring(self, s):
        occ = set()
        n = len(s)

        rk = -1
        ans = 0

        for i in range(n):
            # if i != 0:
            #     occ.remove(s[i-1])

            while rk + 1 < n and s[rk+1] not in occ:
                occ.add(s[rk+1])
                rk += 1

            ans = max(ans, rk - i + 1)

        return ans


if __name__ == '__main__':
    s = Solution()
    # print(s.lengthOfLongestSubstring("abcabcab"))
    print(s.lengthOfLongestSubstring('""'))
