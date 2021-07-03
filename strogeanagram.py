#Sort both strings
#Compare the sorted strings
def areAnargram(str1, str2):
    n1 = len(str1)
    n2 = len(str2)
    if n1 != n2:
        return 0
    print("string")
    str1 = sorted(str1)
    str2 = sorted(str2)

    for i in range (0, n1):
        if str1[i] != str2[1]:
            return 0
    return 1

str1 = input("enter the anagram str1 =")
str2 = input("enter the anagram str2 =")
if areAnargram(str2,str1):
    print("string are equal")
else:
    print("string are not equal")
# Compare the sorted strings


