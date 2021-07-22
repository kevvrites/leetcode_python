# Author: Kevin Liu
# Problems available at https://leetcode.com/
# Start Date: 07/21/2021
# Start Time: 04:06 PM ET
# Complete Date:
# Complete Time:
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

nums_1 = [2,7,11,15]
target_1 = 9

nums_2 = [3,2,4]
target_2 = 6

nums_3 = [3,3]
target_3 = 6

# Brute Force Attempt (doesn't work)
# def two_sum(nums, target):
#     for i in nums:
#         for j in nums:
#             sum1 = i + j
#             if sum1 == target:
#                 if nums.index(i) != nums.index(j):
#                     return nums.index(i), nums.index(j)

def find_index(list, item):
    for i in list:
        if list.count(item) > 1
        if i == item:
            return list.index(i)

# Subtraction Method Attempt
def twoSum(nums, target):
    ans = []
    for i in nums:
        sol = target - i
        if nums.count(sol) >= 1:
            num_loc = nums.index(i)
            sol_loc = nums.index(sol)
            if num_loc != sol_loc:
                ans.append(num_loc)
                ans.append(sol_loc)
                print(ans)
                break
            # else:
            #     sol_loc = nums.reverse().index(sol)
            #     ans.append(num_loc)
            #     ans.append(sol_loc)
            #     print(ans)
            #     break

# Filter answers:
# Issue 1: Running against duplicate pairs (e.g. [1,2] is the same as [2,1] but both are returned)
# Issue 2: Running against using the same number twice (e.g. [0,0])
# Solution Attempt: checking if the indexes are equal resolves issue 2.
# Solution Attempt: end the loop after one answer is printed resolves issue 1.



twoSum(nums_1, target_1)
twoSum(nums_2, target_2)
twoSum(nums_3, target_3)
