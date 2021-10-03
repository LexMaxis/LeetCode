'''
给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

'''
class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums) == 0:
            return 0
        slowIndex = 0

        for fastIndex in range(0, len(nums) - 1):
            if nums[fastIndex] != nums[fastIndex + 1]:
                slowIndex += 1
                nums[slowIndex] = nums[fastIndex + 1]
        return slowIndex+1