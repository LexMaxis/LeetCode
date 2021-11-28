class Solution(object):
    def targetIndices(self, nums, target):
        order_list = []
        nums.sort()

        for i in range(len(nums)):
            if nums[i] > target:
                break
            if nums[i] == target:
                order_list.append(i)

        return order_list


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 5, 2, 3]
    target = 5
    s.targetIndices(nums,target)