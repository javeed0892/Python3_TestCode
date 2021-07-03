lists = ["apple", "banana", "cherry"]
new_list = []
for x in lists:
    if "a" in x:
        new_list.append(x)
print(new_list)
### with comprehension you can do all that with only one line code:
lists = ["apple", "banana", "cherry"]
# comprehensionlist = [x for x in lists if "r" in x]##newlist = [expression for item in iterable if condition == True]
# print(comprehensionlist)
new_list = [x for x in lists] #if x != "apple"]
print(new_list)
new_range  = [x for x in range(10) if x <5 ]
print(new_range)
fruitslist = ["apple", "banana","cherry", "kiwi"]#
new_fruitslist = [x if x != "banana" else "orange" for x in fruitslist]##The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome:
print(new_fruitslist)
# for x in lists:
# #     print(x)
# for x in range(len(lists)):
#     print(lists)
# # i = 0
# while i < len(lists):
#     print(lists)
#     i += 1
###short hand for loop
# [print(lists) for x in lists]

