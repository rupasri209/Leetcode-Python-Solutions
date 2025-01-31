"""
PROBLEM LINK: https://leetcode.com/problems/single-number/description/
"""
class Solution(object):
    def singleNumber(self, nums):
        result = 0
        for num in nums:
            result ^= num
        return result
