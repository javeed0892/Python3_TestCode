from typing import List
class Solution:
    def maxSubArray(nums: List[int]) -> int:
        # maxsum, currentsum = nums[0], nums[0]
        # for i in nums[1:]:
        #     currentsum = max(i, currentsum + i)
        #     maxsum = max(maxsum, currentsum)
        # return maxsum
        maxsums, currentsums = nums[0], nums[0]
        for i in nums[1:]:
            currentsums = max(i, currentsums + i)
            maxsums = max(maxsums, currentsums)
        return maxsums
nums = [-2,1,-3,4,-1,2,1,-5,4]
subarry = Solution
print(Solution.maxSubArray(nums))