# # class Solution:
# #     def ispolindrome(x:int)->bool:
# #         x = str(x)
# #         return x == x[::-1]
# # x = 121
# # p1 = Solution
# # print(p1.ispolindrome(x))
# class Solution:
#     def reverse(x: int) -> int:
#         limit = pow(2, 31) -1
#         if x > 0 and x<= limit:
#             number = str(abs(x))
#             #num = list(number)
#             #join = "".join(reversed(number))
#             palindrome = number[::-1]
#             req = int(palindrome)
#             if req <= limit:
#                 return req
#         if x < 0 and -limit <= x:
#             number = str(abs(x))
#             #num = list(number)
#             #join = "".join(reversed(number))
#             palindrome = number[::-1]
#             req = -int(palindrome)
#             if -limit <= req:
#                 return req
#         return 0
# x = -123
# p1 = Solution
# print(p1.reverse(x))
#
# >>> l = ['abc', 'adb', '9283a74bg', 'boys and girls']
# >>> sets = [set(x) for x in l]
# >>> set[0].intersection(*sets[1:])
# set(['b', 'a'])

