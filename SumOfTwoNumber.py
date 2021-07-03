from typing import List


class Solution:
    def twoSum(nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            for j in range(0, i):
                if (nums[j] + nums[i]) == target:
                    return (j, i)
nums = [2,7,11,15]
target = 9
sums = Solution
print(sums.twoSum(nums, target))