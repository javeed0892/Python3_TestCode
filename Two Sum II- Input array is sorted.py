from typing import List


class Solution:
    def twoSum( numbers: List[int], target: int) -> List[int]:
        for i in range (0, len(numbers)): #0 2
            for j in range(0, i):
                if numbers[j]+ numbers[i] == target:
                    return (j+1,i+1)

numbers = [-1,0]
target = -1
sums = Solution
print(sums.twoSum(numbers,target))