class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
    """
    :type head: Optional[ListNode]
    :rtype: Optional[ListNode]
    """

    prev, curr = None, head
    while curr:
        next_node = curr.next # next_node=2
        curr.next = prev # 2 = None
        prev = curr # prev = 1
        curr = next_node # curr = 2

    return prev

head = ListNode(1)
a = ListNode(2)
b = ListNode(3)
c = ListNode(4)
d = ListNode(5)

head.next(a)
a.next(b)
b.next(c)
c.next(d)
assert reverseList(head) == [5,4,3,2,1], "Wrong"