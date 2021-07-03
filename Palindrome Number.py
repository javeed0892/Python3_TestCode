class Solution:
    def isPalindrome(x: int) -> bool:
        x = str(x)
        return x == x[::-1]

x =123
palidrome = Solution
print(palidrome.isPalindrome(x))