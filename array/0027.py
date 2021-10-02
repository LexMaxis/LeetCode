class Solution(object):
    # false
    def removeElementForce(self, nums, val):
        size = len(nums)
        for i in range(0, len(nums)):
            if nums[i] == val:
                for j in range(i + 1, len(nums)):
                    nums[j - 1] = nums[j]
                i -= 1
                size -= 1

        print(nums)
        print(size + 1)
        return size

    def removeElement(self, nums, val):
        N = len(nums)
        count = -1
        for i in range(N):
            if nums[i] != val:
                count += 1
                nums[count] = nums[i]
        return count + 1


if __name__ == '__main__':
    nums = [3, 2, 2, 3]
    s = Solution()
    s.removeElement(nums, 3)
