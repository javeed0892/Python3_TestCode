class Solution:
    def longestCommonPrefix(strs) -> str:
        x = ''
        n = min([len(i) for i in strs]) #min flow
        for i in range(n): #0,4
            flag = True
            for j in range(len(strs)-1):#0,2
                if strs[j][:i+1] != strs[j+1][:i+1]:# 1 2 != 2 2
                    return x
            x = strs[0][:i+1]
        return x
strs = ["flower","flow","flight"]
strsing = Solution
print(strsing.longestCommonPrefix(strs))