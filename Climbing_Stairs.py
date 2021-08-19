# Author: Kevin Liu
# Problems available at https://leetcode.com/
# Start Date: 08/19/2021
# Start Time: 03:40 PM ET
# Complete Date: 08/19/2021
# Complete Time: 04:00 PM ET
# Note: Problem may or may not be completed in one sitting.

# Climbing Stairs
# https://leetcode.com/problems/climbing-stairs/

# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Example Cases
# Example 1:
# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

# Example 2:
# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

# Constraints
# 1 <= n <= 45
# ------------------------------------------------------------------------------------------------------------------------------------
# Thought process:
# 1. How many possible permutations are there? all 1s, then all 2s, then in between. Similar to binary count.
# 2. 2+1 is distinct from 1+2.
# 3. Inefficient: use a counter and cycle through every possible permutation.
# 4. Using math, the equation is x + 2y = n. Find all possible combinations of x and y (x and y are integers) given n.
# 5. If the number n increases by 1, and it is odd, then there are small_step additional permutation. (e.g. 2->3 returns 2->3)
# 6. If the number n increases by 2, and it is even, then there are big_step additional permutations (e.g. 3->4 returns 3->5)
# 7. Update the small_step to become big_step, and then update the big_step to be the total count.
# 8. This is also the fibonacci sequence.

def climbstairs(n):
    small_step = 1
    big_step = 2
    count = 0
    if n <= 3:
        return n
    for steps in range(2, n):
        count = small_step + big_step
        small_step = big_step
        big_step = count
    return count

# Submission Result:
# Runtime:      0024 ms (top 00.00%)
# Memory Usage: 00.0 MB (top 00.00%)