class Solution:
    def __init__(self,s):
        self.s = s
    def isvaild(self):
        ln = len(s)
        if ln % 2:
            return False
        stack = ['']
        dict = {')':'(', '}':'{', ']':'['}
        for c in s:
            if c in ['(','[','{']:
                stack.append(c) # )
            elif dict[c] != stack[-1]: # ( != (
                return False
            else:
                stack.pop()
        return stack[-1] == ''
s = "[]"
s1 = Solution
print(s1.isvaild(s))