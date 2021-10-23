'''
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。
'''
class Solution(object):
    def longestCommonPrefix(self, strs):
        temp = ''
        flag = 0
        for i in range(len(strs[0])):
            if flag == 0:
                temp = str(temp) + str(strs[0][i])
                for j in (1, len(strs)):
                    if temp in str(strs[j]):
                        continue
                    else:
                        flag = 1
                        break
            else:
                break
        return temp

if __name__ == '__main__':
    s = Solution()
    strs = ["flower", "flow", "flight"]
    print(s.longestCommonPrefix(strs))
