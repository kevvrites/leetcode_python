# Author: Kevin Liu
# Problems available at https://leetcode.com/
# Start Date: 08/04/2021
# Start Time: 12:45 PM ET
# Complete Date: 00/00/0000
# Complete Time: 00:00 PM ET
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
# The first word should have the full prefix.
# The second loop will reduce the prefix to only the matching parts.
# The third loop will reduce the prefix further, etc.
# Return the prefix.
# .substring might be really helpful
# map may also be helpful

def longestCommonPrefix(strs):
    if len(strs) <= 1:
        prefix = strs[0]
        return prefix
    prefix = strs[0]
    for word in range(len(strs)):
        word = strs[word]
        nextword = strs[word + 1]
        if map(checkString(word, nextword), strs):
            prefix += word
    return prefix

def checkString(sub, word):
    if sub in word:
        return True

# Submission Result:
# Runtime:      0000 ms (top 00.00%)
# Memory Usage: 00.0 MB (top 00.00%)

strs = ["flower", "flow"]
print(longestCommonPrefix(strs))



def longestCommonPrefix_1(strs):
    prefix = ""
    letter = 0
    length = len(strs)
    if length <= 1:
        prefix = strs[0]
    else:
        for word in range(length):
            for nextword in range(word + 1, length):
                if strs[word][letter] == strs[nextword][letter]:
                    prefix += strs[word][letter]
                    letter += 1
    return prefix

# Issues:
# The code works for a two-item comparison. It loops through, but it is not effective for comparing three or more objects together.
# The prefix += has to be moved or given a stricter condition.