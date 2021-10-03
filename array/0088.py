class Solution(object):
    def merge(self, nums1, m, nums2, n):
        nums1_index = 0
        nums2_index = 0
        while nums1_index < m and nums2_index < n:
            if nums1[nums1_index] <= nums2[nums2_index] <= nums1[nums1_index + 1]:
                nums1_index += 1

            else:
                temp = nums2[nums2_index]
                nums2[nums2_index] = nums1[nums1_index]
                nums1[nums1_index] = temp
                nums1_index += 1
                nums2_index += 1

        for i in range(0, n):
            nums1[m + i] = nums2[i]

        nums1.sort()

        return nums1