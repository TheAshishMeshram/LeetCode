class Solution:
    def maxSubArray(self, nums):
        curr = nums[0]
        best = nums[0]

        for n in nums[1:]:
            curr = max(n, curr + n)
            best = max(best, curr)

        return best