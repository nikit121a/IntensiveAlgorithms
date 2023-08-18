from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        curr = 0
        plus = False
        for i in nums:
            if i > 0:
                plus = True
                break
        if not plus:
            return max(nums)

        for i in nums:
            curr += i
            if curr > maxSum:
                maxSum = curr
            if curr < 0:
                curr = 0
        return maxSum

# https://leetcode.com/problems/maximum-subarray/
