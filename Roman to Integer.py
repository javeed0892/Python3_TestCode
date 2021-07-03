class Solution:
    def romanToInt(s: str) -> int:
        sum = 0
        i = 0
        roman_dict = {
            'M': 1000,
            'CM': 900,
            'D': 500,
            'CD': 400,
            'C': 100,
            'XC': 90,
            'L': 50,
            'XL': 40,
            'X': 10,
            'IX': 9,
            'V': 5,
            'IV': 4,
            'I': 1
        }
        lenght = len(s) # 3
        while i < lenght: # 2 < 3
            if i < lenght -1 and (s[i] + s[i + 1]) in roman_dict:
                sum += roman_dict[s[i] + s[i + 1]]
                i += 2
            else:
                sum += roman_dict[s[i]]
                i += 1
        return sum
s = "III"
roman = Solution
print(roman.romanToInt(s))
