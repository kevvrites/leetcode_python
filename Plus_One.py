# Author: Kevin Liu
# Problems available at https://leetcode.com/
# Start Date: 00/00/0000
# Start Time: 00:00 PM ET
# Complete Date: 00/00/0000
# Complete Time: 00:00 PM ET
# Note: Problem may or may not be completed in one sitting.

# Plus One
# https://leetcode.com/problems/plus-one/

# Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.

# The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.

# You may assume the integer does not contain any leading zero, except the number 0 itself.

# Example Cases
# Example 1:
# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.

# Example 2:
# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.

# Example 3:
# Input: digits = [0]
# Output: [1]

# Constraints
# 1 <= digits.length <= 100
# 0 <= digits[i] <= 9
# ------------------------------------------------------------------------------------------------------------------------------------
# Thought process:
# 1. Take an input of a list of digits. Take the last number in the list and add one to it.
# 2. Return the list with the modified digit
# 3. Edge case: if a nine is incremented, then the prior digit must be incremented and the last digit reduced to 0.
# 4. Convert the list of digits to an integer, then add one, then convert back to a list.

# Test Cases

def plus_one(digits):
    digits_plus_one = []
    num = 0
    for i in range(len(digits)):
        conv = digits[i] * 10**(len(digits) - 1 - i)
        num += conv
    num = str(num + 1)
    for each in num:
        digits_plus_one.append(int(each))
    return digits_plus_one

# Submission Result:
# Runtime:      0032 ms (top 32.81%)
# Memory Usage: 14.2 MB (top 51.76%)