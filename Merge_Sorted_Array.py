# Author: Kevin Liu
# Problems available at https://leetcode.com/
# Start Date: 08/19/2021
# Start Time: 04:08 PM ET
# Complete Date: 08/19/2021
# Complete Time: 04:45 PM ET
# Note: Problem may or may not be completed in one sitting.

# Merge Sorted Array
# https://leetcode.com/problems/merge-sorted-array/

# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

# Example Cases
# Example 1:
# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

# Example 2:
# Input: nums1 = [1], m = 1, nums2 = [], n = 0
# Output: [1]
# Explanation: The arrays we are merging are [1] and [].
# The result of the merge is [1].

# Example 3:
# Input: nums1 = [0], m = 0, nums2 = [1], n = 1
# Output: [1]
# Explanation: The arrays we are merging are [] and [1].
# The result of the merge is [1].
# Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.

# Constraints
# nums1.length == m + n
# nums2.length == n
# 0 <= m, n <= 200
# 1 <= m + n <= 200
# -109 <= nums1[i], nums2[j] <= 109
# ------------------------------------------------------------------------------------------------------------------------------------
# Thought process:
# 1. The array nums2 should be merged into nums1. Most likely, it will use a for loop with the length of nums2 as the number of iterations.
# 2. Identify where the number should go from nums2 to num1 (index position). Then, insert it using the .insert(index, item) method.
# 3. May need to .pop() the zeros in the nums1 list, but maybe not. Check later. pop may cause errors due to return.

# Another method:
# 1. Combine both arrays first. Then sort the single array using comparison sorts.

# Fastest method?:
# 1. Combine both arrays. Use built-in sort method to sort the array.

# Fast Method
def merge(nums1, m, nums2, n):
    for i in range(n):
        nums1.pop()
    nums1.extend(nums2)
    nums1.sort()

# Submission Result:
# Runtime:      0036 ms (top 30.16%)
# Memory Usage: 14.2 MB (top 13.56%)

# ------------------------------------------------------------------------------------------------------------------------------------

# Method1 Attempt
# def merge(nums1, m, nums2, n):
#     for i in range(n):
#         j = 0
#         if nums2[i] <= nums1[j]:
#             nums1.insert(j, nums2[i])
#             nums1.pop()
#         if nums2[i] >= nums1[m - n - 1]:
#             nums1.insert(m-n, nums2[i])
#             nums1.pop()
#     for num in range(m):
#         if num != (m - 1):
#             if nums1[num] > nums1[num + 1]:
#                 nums1.
#     return nums1