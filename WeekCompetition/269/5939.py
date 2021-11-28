class Solution(object):
    def getAverages(self, nums, k):
        avgs = []
        total_temp = 0
        if len(nums) <= 2*k - 1:
            return [-1]
        if k == 0:
            return nums
        else:
            for p in range(k):
                avgs.append(-1)

            for j in range(2*k+1):
                total_temp += nums[j]

            for i in range(k, len(nums)-k):
                avg_temp = int(total_temp / (2 * k + 1))
                total_temp = total_temp - nums[i-k] + nums[len(nums)-k+1-i]
                avgs.append(avg_temp)

            for r in range(k):
                avgs.append(-1)

        return avgs


if __name__ == '__main__':
    s = Solution()
    nums = [40527,53696,10730,66491,62141,83909,78635,18560]
    k =  2
    print(s.getAverages(nums,k))