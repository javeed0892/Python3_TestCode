# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def mergeTwoLists(self,l1,l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ret = ListNode(0) # 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6
        p = ret # 5
        while True:
            if l1 == None:
                p.next = l2 # 5-> 6
                break
            if l2 == None:
                p.next = l1
                break
            if l1.val < l2.val:
                p.next = l1 #2->3->4->5
                p = p.next #5
                l1  = l1.next #None
            else:
                p.next = l2 #1->2->3 ->4
                p = p.next #4
                l2 = l2.next #6
        return ret.next


l1 = ListNode(1);
l1.next = ListNode(3); #
l1.next.next = ListNode(5);
l2 = ListNode(2);
l2.next = ListNode(4);
l2.next.next = ListNode(6);
test = Solution()
result = test.mergeTwoLists(l1,l2);

while result != None:
    print(result.val)
    result = result.next
