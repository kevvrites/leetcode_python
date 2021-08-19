# Author: Kevin Liu
# Problems available at https://leetcode.com/
# Start Date: 08/19/2021
# Start Time: 10:06 AM ET
# Complete Date: 00/00/0000
# Complete Time: 00:00 PM ET
# Note: Problem may or may not be completed in one sitting.

# Sqrt(x)
# https://leetcode.com/problems/sqrtx/

# Given a non-negative integer x, compute and return the square root of x.

# Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

# Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.

# Example Cases
# Example 1:
# Input: x = 4
# Output: 2

# Example 2:
# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.

# Constraints
# 0 <= x <= 231 - 1
# ------------------------------------------------------------------------------------------------------------------------------------
# Thought process:
# 1. Slow method, but working: check every number up to x and compare the squares. Once you find the number that is bigger squared, then return the previous number.
# 2. Edge case: 0 is 0, 1 is 1.

def my_sqrt(x):
    for i in range(x + 1):
        chk = i * i
        if chk > x:
            return i - 1
        if chk == x:
            return i
    return 0

# Submission Result:
# Runtime:      2408 ms (top 87.67%)
# Memory Usage: 14.3 MB (top 59.07%)

# How to improve it: BINARY SEARCH
# Check the middle number first: if it is too high, then the numbers past that are all too high.
# Then check the middle number of that range.

def my_sqrt(x):
    if x == 0 or x == 1:
        return x
    start = 1
    end = x

    while start <= end:
        mid = (start + end) // 2
        sq = mid * mid
        if sq == x:
            return mid
        if sq < x:
            start = mid + 1
            ans = mid
        else:
            end = mid - 1
    return ans

# Submission Result:
# Runtime:      0040 ms (top 47.24%)
# Memory Usage: 14.1 MB (top 29.30%)