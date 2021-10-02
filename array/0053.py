'''
给定一个整数数组 nums ，
找到一个具有最大和的连续子数组（子数组最少包含一个元素），
返回其最大和
'''


class Solution(object):
    # [first attempt]
    # def maxSubArrayForce(self, nums):
    #     sum = 0
    #     nums.sort(reverse=True)
    #     for i in range(len(nums)):
    #         if nums[i] >= 0:
    #             sum += nums[i]
    #         else:
    #             break
    #     return sum


    def maxSubArrayForce(self, nums):
        pass


if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    s = Solution()
    s.maxSubArrayForce(nums)