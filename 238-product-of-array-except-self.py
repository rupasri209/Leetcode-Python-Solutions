"""
PROBLEM LINK: https://leetcode.com/problems/product-of-array-except-self/description/
"""
#SOLUTION 1:
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left_product = [1 for i in range(len(nums))]
        right_product = [1 for i in range(len(nums))]
        result = []
        for i in range(1, len(nums)):
                left_product[i] = nums[i - 1] * left_product[i - 1]
        for i in range( len(nums) - 2, -1, -1):
                right_product[i] = nums[i + 1] * right_product[i + 1]
        for i in range(len(nums)):
            result.append(left_product[i] * right_product[i])
        return result

#SOLUTION 2:
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [1 for i in range(len(nums))]
        right_product = 1
        for i in range(1, len(nums)):
            result[i] = nums[i - 1] * result[i - 1]
        for i in range(len(nums) - 1 , -1 , -1):
            result[i] *= right_product
            right_product *= nums[i]
        return result