class Solution:
    def findPaths(m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        def rec(row, col, availMove):
            if availMove > -1:
                if row < 0: return 1
                if col < 0: return 1
                if row >= m : return 1
                if col >= n : return 1
            else: return 0
            x = rec(row - 1, col, availMove - 1)
            x += rec(row + 1, col, availMove - 1)
            x += rec(row, col - 1, availMove - 1)
            x += rec(row, col + 1, availMove - 1)
            return x
        return rec(startRow, startColumn, maxMove) % 1000000007

m = 2
n = 2
maxMove = 2
startRow = 0
startColumn = 0
recursion = Solution
print(recursion.findPaths(m,n,maxMove,startRow,startColumn))