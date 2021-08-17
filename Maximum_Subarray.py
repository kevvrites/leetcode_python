# Author: Kevin Liu
# Problems available at https://leetcode.com/
# Start Date: 08/17/2021
# Start Time: 01:10 PM ET
# Complete Date: 08/17/2021
# Complete Time: 01:46 PM ET
# Note: Problem may or may not be completed in one sitting.

# Maximum Subarray
# https://leetcode.com/problems/maximum-subarray/

# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# A subarray is a contiguous part of an array.

# Example Cases
# Example 1:
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

# Example 2:
# Input: nums = [1]
# Output: 1

# Example 3:
# Input: nums = [5,4,-1,7,8]
# Output: 23

# Constraints
# 1 <= nums.length <= 3 * 10**4
# -105 <= nums[i] <= 105
# ------------------------------------------------------------------------------------------------------------------------------------
# Thought process:
# 1. Brute force would be to find the sum of all the numbers, then start taking out numbers on the edges. (Generate all subarrays)
# 2. Replace the maximum sum counter with a higher sum if found.

# Note: This problem uses something called Kadane's Algorithm
# Kadane's Algorithm Process:
# Start with the first number of the array.
# For the next number, compare between two options: either add the number to the existing array, or start a new array.
# This is chosen using the TOTAL SUM of the existing array up to that point.

def bf_max_subarray(nums):
    for i in range(len(nums)):
        current_sum = nums[i]
        for j in range(1, len(nums)):
            current_sum += nums[j]
            max_sum = max(current_sum, max_sum)
    return max_sum

def max_subarray(nums):
    current_sum = nums[0]
    max_sum = current_sum
    for i in range(1, len(nums)):
        if current_sum + nums[i] > nums[i]:
            current_sum += nums[i]
        else:
            current_sum = nums[i]
        max_sum = max(max_sum, current_sum)
    return max_sum

# Submission Result:
# Runtime:      0068 ms (top 51.59%)
# Memory Usage: 14.9 MB (top 14.23%)

def max_subarray_v2(nums):
    current_sum = nums[0]
    max_sum = current_sum
    for i in range(1, len(nums)):
        current_sum = max(current_sum + nums[i], nums[i])
        max_sum = max(max_sum, current_sum)
    return max_sum

# Submission Result:
# Runtime:      0060 ms (top 09.39%)
# Memory Usage: 15.0 MB (top 14.23%)