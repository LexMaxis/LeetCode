class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums1.extend(nums2)
        nums1.sort()
        n = len(nums1)
        ans = 0
        if n % 2 == 0:
            ans = (nums1[int(n / 2)] + nums1[int(n / 2) - 1]) / 2
        else:
            ans = nums1[int(n / 2)]

        return ans


if __name__ == '__main__':
    nums1 = [1, 2]
    nums2 = [3, 4]
    s = Solution()
    print(s.findMedianSortedArrays(nums1, nums2))
