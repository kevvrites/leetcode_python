# Author: Kevin Liu
# Problems available at https://leetcode.com/
# Start Date: 08/16/2021
# Start Time: 02:16 PM ET
# Complete Date: 08/16/2021
# Complete Time: 02:31 PM ET
# Note: Problem may or may not be completed in one sitting.

# Implement strStr()
# https://leetcode.com/problems/implement-strstr/

# Implement strStr().

# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# Clarification:

# What should we return when needle is an empty string? This is a great question to ask during an interview.

# For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

# Example Cases
# Example 1:
# Input: haystack = "hello", needle = "ll"
# Output: 2

# Example 2:
# Input: haystack = "aaaaa", needle = "bba"
# Output: -1

# Example 3:
# Input: haystack = "", needle = ""
# Output: 0

# Constraints
# 0 <= haystack.length, needle.length <= 5 * 104
# haystack and needle consist of only lower-case English characters.
# ------------------------------------------------------------------------------------------------------------------------------------
# Thought process:
# 1. Base case: return 0 when the string is empty.
# 2. Use a counter to keep track of the index across the for loop.
# 3. If the counter is equal to the length of the haystack, return -1 as the needle was not found in the haystack.

# Test Cases
haystack = "mississippi"
needle = "issip"

def strStr(haystack, needle):
    count = 0
    length = len(needle)
    if len(needle) == 0:
        return 0
    for letter in haystack:
        if letter != needle[0]:
            count += 1
        else:
            bit = haystack[count:count + length]
            if bit == needle:
                return count
            count += 1
    return -1

# Submission Result:
# Runtime:      0072 ms (top 86.48%)
# Memory Usage: 14.6 MB (top 89.83%)