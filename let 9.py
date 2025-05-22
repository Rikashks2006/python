def removeNthFromEnd(self, head, n):
    fast = slow = dummy = ListNode(0)
    dummy.next = head
    for _ in xrange(n):
        fast = fast.next
    while fast and fast.next:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return dummy.next
