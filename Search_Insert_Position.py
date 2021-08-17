# Author: Kevin Liu
# Problems available at https://leetcode.com/
# Start Date: 08/17/2021
# Start Time: 12:58 PM ET
# Complete Date: 08/17/2021
# Complete Time: 01:08 PM ET
# Note: Problem may or may not be completed in one sitting.

# Search Insert Position
# https://leetcode.com/problems/search-insert-position/

# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

# Example Cases
# Example 1:
# Input: nums = [1,3,5,6], target = 5
# Output: 2

# Example 2:
# Input: nums = [1,3,5,6], target = 2
# Output: 1

# Example 3:
# Input: nums = [1,3,5,6], target = 7
# Output: 4

# Example 4:
# Input: nums = [1,3,5,6], target = 0
# Output: 0

# Example 5:
# Input: nums = [1], target = 0
# Output: 0

# Constraints
# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums contains distinct values sorted in ascending order.
# -104 <= target <= 104
# ------------------------------------------------------------------------------------------------------------------------------------
# Thought process:
# 1. Check if the target is in the list. If it is, use .index to find and return the index.
# 2. If the target is not in the list, loop over the items in the list.
# 3. If the item is larger, then the index of the item is the index that the target would have if it was in the list.
# 4. Edge case: if the target is the largest, then return the length of the list.

def search_insert(nums, target):
    if target in nums:
        ans = nums.index(target)
        return ans
    for num in nums:
        if num > target:
            ans = nums.index(num)
            return ans
    return len(nums)
        

# Submission Result:
# Runtime:      0052 ms (top 66.90%)
# Memory Usage: 15.2 MB (top 76.01%)