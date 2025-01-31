"""
PROBLEM LINK: https://leetcode.com/problems/fibonacci-number/description/
"""
#ITERATIVE SOLTUION
class Solution(object):
    def fib(self, n):
        result = [0, 1]
        if n < 2:
            result[n]
        for i in range(2, n + 1):
            result.append(result[i - 1] + result[i - 2])
        return result[n]

#RECURSIVE SOLUTION - Not suggestible for large numbers
class Solution(object):
    def fib(self, n):
        if n < 2:
            return n
        else:
            return self.fib(n - 1) + self.fib(n - 2)
