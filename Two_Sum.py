# Author: Kevin Liu
# Problems available at https://leetcode.com/
# Start Date: 07/21/2021
# Start Time: 04:06 PM ET
# Complete Date: 08/01/2021
# Complete Time: 12:47 PM ET
# Note: Problem may or may not be completed in one sitting.

# Two Sum
# https://leetcode.com/problems/two-sum/

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]

# Constraints:

# 2 <= nums.length <= 10**4
# -10**9 <= nums[i] <= 10**9
# -10**9 <= target <= 10**9
# Only one valid answer exists.

# Follow-up: Can you come up with an algorithm that is less than 0(n**2) time complexity?

# ------------------------------------------------------------------------------------------------------------------------------------
# Thought process:
# Brute force method: evaluate all the pairs possible and check against target sum.
# 1. Eliminate the numbers in the array that are larger than the target. (optional)
# 2. Iterate over the loop (nested for loop): save a sum in a variable and check with target
# 3. If the answer is found, break the loop and return the arguments.

# Subtraction method:
# 1. Take the first number that is less than the target.
# 2. Search for the missing number within the array (target-current number)
# 3. Return the index of the first number and the index of the second.
# 4. If the index of the subtraction results in null, pick a new first number.

# Subtraction method improved:
# Create a dictionary that stores the subtraction result needed and the index it corresponds to.
# First pass through the array: add the necessary value to the dictionary.
# If the needed value is found in the nums array, then return the index of the original (value in dictionary) and the index of the key value.

# Test Cases
nums_1 = [2,7,11,15]
target_1 = 9

nums_2 = [3,2,4]
target_2 = 6

nums_3 = [3,3]
target_3 = 6

# ------------------------------------------------------------------------------------------------------------------------------------

# Brute Force Method: Time complexity O(n**2)
def bruteForce_twoSum(self, nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            sum1 = nums[i] + nums[j]
            if sum1 == target:
                return [i, j]

# Brute Force Submission Result:
# Runtime:      4544 ms (top 86.94%)
# Memory Usage: 14.9 MB (top 34.83%)

# ------------------------------------------------------------------------------------------------------------------------------------

# Subtraction Method Attempt: Time complexity O(n**2)
def subtraction_twoSum(self, nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            searchFor = target - nums[i]
            if nums[j] == searchFor:
                return [i, j]

# Subtraction Submission Result:
# Runtime:      4492 ms (top 86.05%)
# Memory Usage: 14.8 MB (top 07.97%)

# ------------------------------------------------------------------------------------------------------------------------------------

# Dictionary Method Attempt: Time complexity O(n)
def dict_twoSum(nums, target):
    answers = {}
    for i in range(len(nums)):
        num = nums[i]
        searchFor = target - num

        if num in answers:
            return [i, answers[num]]
        else:
            answers[searchFor] = i

dict_twoSum(nums_1, target_1)

# Dictionary Submission Attempt:
# Runtime:      0060 ms (top 23.11%)
# Memory Usage: 15.6 MB (top 85.98%)