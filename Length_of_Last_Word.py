# Author: Kevin Liu
# Problems available at https://leetcode.com/
# Start Date: 08/17/2021
# Start Time: 02:30 PM ET
# Complete Date: 08/17/2021
# Complete Time: 02:38 PM ET
# Note: Problem may or may not be completed in one sitting.

# Length of Last Word
# https://leetcode.com/problems/length-of-last-word/

# Given a string s consisting of some words separated by some number of spaces, return the length of the last word in the string.

# A word is a maximal substring consisting of non-space characters only.

# Example Cases
# Example 1:
# Input: s = "Hello World"
# Output: 5
# Explanation: The words are "Hello" and "World", both of length 5.

# Example 2:
# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The longest word is "moon" with length 4.

# Example 3:
# Input: s = "luffy is still joyboy"
# Output: 6
# Explanation: The longest word is "joyboy" with length 6.

# Constraints
# 1 <= s.length <= 104
# s consists of only English letters and spaces ' '.
# There will be at least one word in s.
# ------------------------------------------------------------------------------------------------------------------------------------
# Thought process:
# 1. Split the string using spaces as the delimiter.
# 2. Use a -1 index to find the last word of the list.
# 3. Return the length of that word.

def length_of_last_word(s):
    s = s.strip()
    words = s.split(' ')
    return len(words[-1])

# Submission Result:
# Runtime:      0020 ms (top 01.03%)
# Memory Usage: 14.2 MB (top 34.85%)