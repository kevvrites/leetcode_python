# Author: Kevin Liu
# Problems available at https://leetcode.com/
# Start Date: 08/20/2021
# Start Time: 11:00 AM ET
# Complete Date: 00/00/0000
# Complete Time: 00:00 PM ET
# Note: Problem may or may not be completed in one sitting.

# Longest Substring Without Repeating Characters
# Problem URL https://leetcode.com/problems/

# Given a string s, find the length of the longest substring without repeating characters.

# Example Cases
# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

# Example 4:
# Input: s = ""
# Output: 0

# Constraints
# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.
# ------------------------------------------------------------------------------------------------------------------------------------
# Thought process:
# 1. Reminds me of the other substring problem maximum_subarray, uses Kadane's algorithm.
# 2. Have a counter starting at 0. Have a temporary variable that stores the current string length.
# 3. If the next character is not the last letter in the string, then add it to the end. Otherwise, start a new string.
# Note: Comment 3 assumes that 'repeating' is referring to adjacent letters. This is not true in this case.
# 4. Replace the counter with the maximum number each iteration.
# 5. Return the counter
# 6. Note: this does not work if the repeating substring is more than 1 letter (e.g. abcabc repeats, so the substring should be "abc").

# Personal Attempt
def length_of_longest_substring(s):
    seen = []
    max_len = 0
    start = 0
    for i in range(len(s)):
        letter = s[i]
        if letter not in seen:
            start += 1
            seen.append(letter)
        else:
            start = 1
        max_len = max(max_len, start)
    return max_len

# Fails on "dvdf" test case.

# ------------------------------------------------------------------------------------------------------------------------------------
# Window Method
# 1. Basically the same process, but add an index tracker
# 2. Create a window, then judge whether the characters repeat (works for longer substrings)

def length_of_longest_substring(s):
    last_index = {}
    max_len = 0
    start_index = 0
    for i in range(len(s)):
        if s[i] in last_index:
            start_index = max(start_index, last_index[s[i]] + 1)
        max_len = max(max_len, i - start_index + 1)
        last_index[s[i]] = i
    return max_len

# Submission Result:
# Runtime:      0064 ms (top 35.28%)
# Memory Usage: 14.4 MB (top 44.65%)

