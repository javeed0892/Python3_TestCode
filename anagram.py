def check (s1, s2):
    if not str:
        return "not a string"

    if (sorted(s1) == sorted(s2)):
        return "anagram is string"
    else:
        return "it's not"

s1 = input(str("enter the anagram string ="))
s2 = input(str("enter the anagram string ="))
check(s1, s2)
print(check(s1,s2))