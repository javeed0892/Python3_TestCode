from typing import List


class Solution:
    def maxSubArray(nums: List[int]) -> int:
        best = nums[0]
        current = nums[0]
        for i in nums[1:]:
            current = max(i, current + i)
            if current > best:
                best = current
        return best
nums = [-2,1,-3,4,-1,2,1,-5,4]
subarry = Solution
print(subarry.maxSubArray(nums))