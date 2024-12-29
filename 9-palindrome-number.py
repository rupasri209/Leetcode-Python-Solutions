"""
PROBLEM LINK: https://leetcode.com/problems/palindrome-number/description/
"""
class Solution:
    def isPalindrome(self, n: int) -> bool:
        if n < 0:
            return False
        rev_num = 0
        temp_num = n
        while temp_num:
            rev_num = rev_num * 10 + temp_num % 10
            temp_num = temp_num//10
        return rev_num == n