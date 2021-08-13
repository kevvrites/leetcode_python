# Author: Kevin Liu
# Problems available at https://leetcode.com/
# Start Date: 08/03/2021
# Start Time: 02:54 PM ET
# Complete Date: 08/03/2021
# Complete Time: 03:28 PM ET
# Note: Problem may or may not be completed in one sitting.

# Roman to Integer
# https://leetcode.com/problems/roman-to-integer/

# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.

# Example Cases
# Example 1:
# Input: s = "III"
# Output: 3

# Example 2:
# Input: s = "IV"
# Output: 4

# Example 3:
# Input: s = "IX"
# Output: 9

# Example 4:
# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.

# Example 5:
# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

# Constraints
# 1 <= s.length <= 15
# s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
# It is guaranteed that s is a valid roman numeral in the range [1, 3999].
# ------------------------------------------------------------------------------------------------------------------------------------
# Thought process:
# 1. Look for special cases (IV, IX, XL, XC, CD, CM). Special cases exist when the letter after has a higher value than the previous.
# 2. If special cases exist, then subtract double the value of the smaller letter from the total sum.
# 3. Add the value of each letter in the string to a total.
# 4. Return an integer.

def romanToInt(s):
    specials = ["IV","IX","XL","XC","CD","CM"]
    romans = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C": 100, "D": 500, "M" : 1000}
    sum = 0
    for letter in s:
        sum += romans.get(letter)
    for char in specials:
        if char in s:
            sum -= (2 *romans.get(char[0]))
    return sum

# Submission Result:
# Runtime:      0044 ms (top 17.36%)
# Memory Usage: 14.2 MB (top 16.29%)