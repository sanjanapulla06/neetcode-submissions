class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        dummy = ListNode(0)
        dummy.next = head

        prev = dummy

        for i in range(left - 1):
            prev = prev.next

        curr = prev.next

        for i in range(right - left):
            next_node = curr.next.next
            move_node = curr.next

            curr.next.next = prev.next
            prev.next = move_node
            curr.next = next_node

        return dummy.next