# Author: Kevin Liu
# Problems available at https://leetcode.com/
# Start Date: 08/01/2021
# Start Time: 01:24 PM ET
# Complete Date: 08/01/2021
# Complete Time: 01:35 PM ET
# Note: Problem may or may not be completed in one sitting.

# Reverse Integer
# https://leetcode.com/problems/reverse-integer/

# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-2**31, 2**31 - 1], then return 0.
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

# Example Cases

# Example 1:
# Input: x = 123
# Output: 321

# Example 2:
# Input: x = -123
# Output: -321

# Example 3:
# Input: x = 120
# Output: 21

# Example 4:
# Input: x = 0
# Output: 0

# Constraints
# -2**31 <= x <= 2**31 - 1

# ------------------------------------------------------------------------------------------------------------------------------------
# Thought process:
# 1. Take an input integer x. Reverse it. 
# 2. Check if reversing x will make it too large or small, then return 0.
# 3. Else, output the reversed number.

# Test Cases
x_1 = 123
x_2 = -123
x_3 = 120
x_4 = 0

def reverse(x):
    reversed = ""
    num = str(x)
    if "-" in num:
        num = num[1:]
        reversed += "-"
    reversed += num[::-1]
    reversed = int(reversed)
    if (reversed > 2**31-1) or (reversed < -2**31):
        return 0
    else:
        return reversed

# Errors:
# Original code did not work for negative numbers (negative sign moved to back of string/num when reversed)

# Submission Result:
# Runtime:      0036 ms (top 57.17%)
# Memory Usage: 14.3 MB (top 87.86%)