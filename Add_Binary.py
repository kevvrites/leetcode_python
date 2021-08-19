# Author: Kevin Liu
# Problems available at https://leetcode.com/
# Start Date: 08/19/2021
# Start Time: 09:28 AM ET
# Complete Date: 08/19/2021
# Complete Time: 09:52 AM ET
# Note: Problem may or may not be completed in one sitting.

# Add Binary
# https://leetcode.com/problems/add-binary/

# Given two binary strings a and b, return their sum as a binary string.

# Example Cases
# Example 1:
# Input: a = "11", b = "1"
# Output: "100"

# Example 2:
# Input: a = "1010", b = "1011"
# Output: "10101"

# Constraints
# 1 <= a.length, b.length <= 104
# a and b consist only of '0' or '1' characters.
# Each string does not contain leading zeros except for the zero itself.
# ------------------------------------------------------------------------------------------------------------------------------------
# Thought process:
# 1. The optimal way probably involves some sort of "staying in binary" without converting to decimal.
# 2. Long method: convert the inputs to decimal, add together, then convert back to binary.

def to_decimal(s):
    length = len(s)
    dec = 0
    for i in range(length):
        if s[i] == '1':
            dec += 2 ** (length - 1 - i)
    return dec
def to_binary(num):
    return "{0:b}".format(int(num))
def add_binary(a,b):
    dec_a = to_decimal(a)
    dec_b = to_decimal(b)
    ans = dec_a + dec_b
    return to_binary(ans)

# Submission Result:
# Runtime:      0036 ms (top 56.48%)
# Memory Usage: 14.4 MB (top 76.33%)

# One line solution: use built-in formatting tools.
def add_binary(a,b):
    return "{0:b}".format(int(a, 2) + int(b, 2))

# Submission Result:
# Runtime:      0028 ms (top 08.77%)
# Memory Usage: 14.1 MB (top 06.30%)