"""
PROBLEM LINK: https://leetcode.com/problems/valid-parentheses/description/
"""
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        brackets = {'(':')','{':'}','[':']'}
        stack = []
        for char in s:
            if char in brackets.keys():
                stack.append(char)
            elif char in brackets.values():
                if not stack or brackets[stack[-1]] != char:
                    return False
                stack.pop()
        return stack == []