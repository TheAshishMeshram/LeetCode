class Solution:
    def subsets(self, nums):
        res = [[]]

        for n in nums:
            res += [curr + [n] for curr in res]

        return res