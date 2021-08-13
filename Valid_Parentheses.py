# Author: Kevin Liu
# Problems available at https://leetcode.com/
# Start Date: 08/13/2021
# Start Time: 02:30 PM ET
# Complete Date: 08/13/2021
# Complete Time: 03:40 PM ET
# Note: Problem may or may not be completed in one sitting.

# Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/

# Problem Description
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.

# Example Cases
# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "()[]{}"
# Output: true

# Example 3:
# Input: s = "(]"
# Output: false

# Example 4:
# Input: s = "([)]"
# Output: false

# Example 5:
# Input: s = "{[]}"
# Output: true

# Constraints
# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.

# ------------------------------------------------------------------------------------------------------------------------------------
# Thought process:
# 1. Have two lists: open bracket, closed brackets.
# 2. Basic check: make sure there are an even number of brackets of each type, otherwise return false.
# 3. A valid string will always have something like (open open open close close close) or (open close open close)
# 4. The order matters. To check, look for the next index of the closing parentheses. If the items in between the original index and next index is a "closed" bracket without an open bracket, it is false.

# Looking at the solution, this is a classic stack problem. I did not know what a stack is previously.
# Stack: Last in, First Out (LIFO)

# Process:
# 1. If the string has an odd length, it must be false.
# 2. Loop through the string. If the bracket is open, add it to the list.
# 3. If it encounters a closing bracket, check the LAST ADDED BRACKET. This is an open bracket if the list is not empty.
# 4. If the closing bracket matches the opening bracket type, remove it from the list.
# 5. The list should be empty at the end of a valid string.

def isValid(s):
    open = ["(", "[", "{"]
    close = [")", "]", "}"]
    stack = []
    if len(s) % 2 != 0:
        return False
    for bracket in s:
        if bracket in open:
            stack.append(bracket)
        elif bracket in close:
            if len(stack) != 0:
                if stack[-1] == open[close.index(bracket)]:
                    stack.pop(-1)
                else:
                    return False
            else:
                return False
    return len(stack) == 0

# Submission Result:
# Runtime:      0024 ms (top 04.60%)
# Memory Usage: 14.3 MB (top 35.36%)

