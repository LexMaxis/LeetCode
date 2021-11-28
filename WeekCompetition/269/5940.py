class Solution(object):
    def minimumDeletions(self, nums):
        nums_temp = []
        for num in nums:
            nums_temp.append(num)
        nums_temp.sort()

        min_pos = nums.index(nums_temp[0])
        max_pos = nums.index(nums_temp[-1])

        if min_pos <= max_pos:
            return min(min(max_pos + 1, len(nums) - min_pos),
                       min_pos + len(nums) - max_pos + 1)
        else:
            return min(
                        min(len(nums) - min_pos + max_pos + 1, len(nums) + min_pos - max_pos + 1),
                        min(min_pos + 1, len(nums) - max_pos)
                       )


if __name__ == '__main__':
    s = Solution()
    nums = [-87,60,-30,-67,74,55,76,-53]
    print(s.minimumDeletions(nums))