# Author: Kevin Liu
# Problems available at https://leetcode.com/
# Start Date: 08/04/2021
# Start Time: 12:45 PM ET
# Complete Date: 08/13/2021
# Complete Time: 10:24 AM ET
# Note: Problem may or may not be completed in one sitting.

# Longest Common Prefix
# https://leetcode.com/problems/longest-common-prefix/

# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example Cases

# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Example 2:
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

# Constraints
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lower-case English letters.

# ------------------------------------------------------------------------------------------------------------------------------------
# Thought process:
# 1. Use a for loop - for the first item, take the first letter and compare it to the first letter of the second word.
# 2. If all the first letters are the same, then take the second letter.
# 3. Output the string with the common prefix.
# 4. May have to use a double for loop to iterate over the items.
# 5. Check prefix with the next character.

# Process:
# The first word is the prefix.
# If the next word does not start with the prefix, then cut the last letter of the prefix.
# Repeat until a prefix matches.
# If a prefix matches, then go to the next word in the list.
# If no matches, then it will return an empty string.

def longestCommonPrefix(strs):
    if len(strs) <= 1:
        prefix = strs[0]
    else:
        prefix = strs[0]
        for i in range(1, len(strs)):
            while not strs[i].startswith(prefix):
                prefix = prefix[:-1]
    return prefix

# Submission Result:
# Runtime:      0042 ms (top 85.96%)
# Memory Usage: 14.3 MB (top 18.10%)