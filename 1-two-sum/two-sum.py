class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsmap = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in numsmap:
                return [numsmap[diff], i]
            numsmap[nums[i]] = i

