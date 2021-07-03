class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(head:ListNode, key: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        while cur and cur.next:
            if cur.next.val == key:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next

l1 = ListNode(1);
l1.next = ListNode(2); #
l1.next.next = ListNode(3);
l1.next.next.next = ListNode(4);
l1.next.next.next.next = ListNode(5);
l1.next.next.next.next.next = ListNode(6);
val = 6
heads = Solution
result = heads.removeElements(l1, 1)

while result != None:
    print(result.val)
    result = result.next
