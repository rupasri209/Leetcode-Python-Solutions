"""
PROBLEM LINK: https://leetcode.com/problems/two-sum/description/
"""
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        complement = {}
        for i in range(len(nums)):
            if(target - nums[i] in complement.keys()):
                return [complement[target - nums[i]], i]
            complement[nums[i]] = i
