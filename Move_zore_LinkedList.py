from typing import List
class Solution:
    def moveZeroes(nums: List[int]) -> None:
        for i in range (0, len(nums)):
            if nums[i] == 0:
                nums.remove(0)
                nums.append(0)
        return nums
nums = [0,1,0,3,12]
moving = Solution
print(moving.moveZeroes(nums))