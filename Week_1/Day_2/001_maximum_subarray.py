class Solution:
    def maxSubArray(self, nums):
        max_sum = nums[0]
        temp = nums[0]
        for i in range(1, len(nums)):
            temp = max(nums[i], temp + nums[i])
            if temp > max_sum:
                max_sum = temp
        return max_sum