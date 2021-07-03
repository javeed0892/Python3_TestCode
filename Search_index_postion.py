from typing import List


class Solution:
    def searchInsert(nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            i = nums
            i.append(target)
            i.sort()
            return i.index(target)
nums = [1,3,5,6]
target =10
search = Solution
print(search.searchInsert(nums,target))
