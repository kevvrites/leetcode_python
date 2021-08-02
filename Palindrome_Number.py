# Author: Kevin Liu
# Problems available at https://leetcode.com/
# Start Date: 08/01/2021
# Start Time: 04:55 PM ET
# Complete Date: 08/01/2021
# Complete Time: 09:00 PM ET
# Note: Problem may or may not be completed in one sitting.

# Palindrome Number
# https://leetcode.com/problems/palindrome-number/

# Given an integer x, return true if x is palindrome integer.

# An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.

# Example Cases
# Example 1:
# Input: x = 121
# Output: true

# Example 2:
# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

# Example 3:
# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

# Example 4:
# Input: x = -101
# Output: false

# Constraints
# -2^31 <= x <= 2^31 - 1
# ------------------------------------------------------------------------------------------------------------------------------------
# Thought process:
# 1. Take an input integer x.
# 2. Convert to a string and reverse it using slicing.
# 3. Check if the reverse is the same as the original, and output true if it is.

# Test Cases

def isPalindrome(x):
    x = str(x)
    new = x[::-1]
    if new == x:
        return True
    else:
        return False

# Submission Result:
# Runtime:      0044 ms (top 98.31%)
# Memory Usage: 14.1 MB (top 77.70%)

# ------------------------------------------------------------------------------------------------------------------------------------
# Follow up: Could you solve it without converting the integer to a string?
# Thought process:
# 1. Check the first and last number and go along that. Will need some loop (likely for loop).
# 2. Find the number of digits to iterate the loop over. Depending on the number.
# 3. Finding the first digit of any number x is x // (10**(digits - 1))
# 4. Finding the second digit of any number x is x // (10**(digits - 2))
# 5. Finding the last digit of any number x is x % (10**(loop count + 1)) // (10**loop count)
# 6. Finding the second to last digit of any number x is x % (10**(loop count + 2)) // (10**loop count + 1)

def isPalindromeInt(x):
    digits = 0
    tempx = x
    if x < 0:
        return False
    while tempx >= 1:
        digits += 1
        tempx = tempx // 10
    loops = digits // 2
    for num in range(loops):
        if num == 0:
            frontnum = (x // (10 ** (digits - (num + 1))))
        else:
            frontnum = (x // (10 ** (digits - (num + 1)))) % (10 ** num)
            if frontnum >= 10:
                frontnum = frontnum % 10
        backnum = ((x % (10 ** (num + 1))) // (10 ** num))
        print(frontnum, backnum)
        if frontnum != backnum:
            return False
    return True


y = 1001001001
print(isPalindromeInt(y))

# Submission Result:
# Runtime:      0132 ms (top 05.14%)
# Memory Usage: 14.3 MB (top 49.48%)

# Errors:
# Cutting frontnum has errors for the first number because you cannot do % 0. 1 % 1 = 0, so the first case is special.
# Odd-number length numbers result in errors because the code will then check a XX number to a X number. The middle number should not be a factor.