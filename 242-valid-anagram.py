"""
PROBLEM LINK: https://leetcode.com/problems/valid-anagram/
"""
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        charS = {}
        for i in range(len(s)):
            charS[s[i]] = 1 + charS.get(s[i], 0)
        for ch in t:
            if ch not in charS or charS[ch] == 0:
                return False
            charS[ch] -= 1
        return True