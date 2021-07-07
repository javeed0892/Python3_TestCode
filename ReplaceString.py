class Solution:
    def defangIPaddr(address: str) -> str:
        return address.replace('.','[.]')

address = "1.1.1.1"
replace = Solution
print(replace.defangIPaddr(address))
