"""
PROBLEM LINK: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
"""
class Solution(object):
    def searchRange(self, nums, target):
        left = self.searchPosition(nums, target, True)
        if left == -1:
            return [-1, -1]
        right = self.searchPosition(nums, target, False)
        return [left, right]

    def searchPosition(self, nums, target, isLeft):
        position = -1
        low, high = 0, len(nums) - 1
        while(low <= high):
            mid = (low + high) // 2
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                if isLeft:
                    high = mid - 1
                else:
                    low = mid + 1
                position = mid
        return position