class Solution:
    def strStr( haystack: str, needle: str) -> int:
        return haystack.find(needle)

haystack = "hello"
needle = "ll"
Findingindex = Solution
print(Findingindex.strStr(haystack,needle))