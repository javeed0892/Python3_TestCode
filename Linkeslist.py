class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next


l1= Node(1)
l1.next = Node(2)
l1.next.next = Node(3)
l1.next.next.next = Node(4)


while l1 != None:
    print(l1.data)
    l1 = l1.next



# 1 -> 2 -> 3 -> 4 -> 5