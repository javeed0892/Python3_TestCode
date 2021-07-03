from typing import List
# class Solution:
#     def removeElement(nums: List[int], val: int) -> int:
#         if len(nums) < 1:
#             return 0
#         i = 0
#         len_chk = len(nums)
#         while i < len_chk:
#             if nums[i] == val:
#                 nums[i] = nums[-1]
#                 nums.pop()
#                 len_chk = len(nums)
#             else:
#                 i += 1
#         return len(nums)
class Solution:
    def removeElement(nums: List[int], val: int) -> int:
        while val in nums:
            nums.remove(val)
        return len(nums)

nums = [0,1,2,2,3,0,4,2]
val = 2
remove = Solution
print(remove.removeElement(nums, val))