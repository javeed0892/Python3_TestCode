class Solution:
    def reverse(x: int) -> int:
        limit = pow(2 , 31 ) -1
        if x > 0 and x < limit:
            numbers = str(abs(x))
            palidrome = numbers[::-1]
            req = int(palidrome)
            if req <= limit:
                return req
        if x < 0 and -limit <= x:
            numbers = str(abs(x))
            palidrome = numbers[::-1]
            req = -int(palidrome)
            if -limit <= req:
                return req
        return 0

x = -456
revers = Solution
print(revers.reverse(x))
