"""
PROBLEM LINK: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
"""
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        charSet, left = set(), 0
        length = 0
        for right in range(len(s)):
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1
            charSet.add(s[right])
            length = max(length, right - left + 1)
        return length