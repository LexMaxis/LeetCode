class Solution(object):
    def searchInsert_bymyself(self, nums, target):
        size = len(nums)
        i = int(size / 2)

        if size == 0:
            return 0

        while nums[i] is not None:
            if nums[i] == target:
                return i
            elif nums[i] > target:
                i = int((i + size) / 2)
                if nums[i] > nums[size - 1]:
                    return size
                elif nums[i] < nums[i]:
                    return i
            elif nums[i] < target:
                i = int(i / 2) + 1
                if nums[i] > nums[i]:
                    return i
                elif nums[i] < nums[0]:
                    return 0

    def searchInsert(self, nums, target):
        n = len(nums)
        left = 0
        right = n-1
        while left <= right:
            mid = left + int((right-left)/2)
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        print(left)
        return left


if __name__ == '__main__':
    nums = [1, 3, 5, 6]
    s = Solution()
    s.searchInsert(nums, 0)
