# Author: Kevin Liu
# Problems available at https://leetcode.com/
# Start Date: 08/01/2021
# Start Time: 01:00 PM ET
# Complete Date: 
# Complete Time: 
# Note: Problem may or may not be completed in one sitting.

# Add Two Numbers
# https://leetcode.com/problems/add-two-numbers/

# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example 1:
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# Example 2:
# Input: l1 = [0], l2 = [0]
# Output: [0]

# Example 3:
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]

# Constraints:

# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading zeros.

# ------------------------------------------------------------------------------------------------------------------------------------
# Thought process:
# 1. Take two lists as input. Multiply each number in the list by *10 depending on their index number to get the 'original' number.
# 2. Add the two numbers together.
# 3. Turn the final number into a string and reverse it.
# 4. Turn the string into a list and return it.

# Test Cases
l1_1 = [2,4,3]
l2_1 = [5,6,4]

l1_2 = [0]
l2_2 = [0]

l1_3 = [9,9,9,9,9,9,9]
l2_3 = [9,9,9,9]

def addTwoNumbers(l1, l2):
    sum1 = 0
    sum2 = 0
    ans = []
    for num in range(len(l1)):
        temp_num = l1[num] * 10**num
        sum1 += temp_num
    for num in range(len(l2)):
        temp_num = l2[num] * 10**num
        sum2 += temp_num
    total = sum1 + sum2
    print(sum1)
    print(sum2)
    print(total)
    total_str = str(total)[::-1]
    for num in total_str:
        ans.append(num)
    return ans

print(addTwoNumbers(l1_1, l2_1))

# 08/01/2021 01:17PM ET Note: The code works for list inputs, but it does not work for linked list inputs.
# I have not yet learned about those, so this program will be put on hold until I learn more.