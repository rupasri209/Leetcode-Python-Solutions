"""
PROBLEM LINK: https://leetcode.com/problems/climbing-stairs/description/
"""
class Solution(object):
    def climbStairs(self, n):
        stepsCount = [1, 1]
        if n < 2:
            stepsCount[n]
        for i in range(2, n + 1):
            stepsCount.append(stepsCount[i - 1] + stepsCount[i - 2])
        return stepsCount[n]