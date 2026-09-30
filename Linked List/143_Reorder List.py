class Solution:
    def reorderList(self, head) -> None:
        if not head or not head.next:
            return

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        previous = None
        current = slow.next
        slow.next = None
        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        first, second = head, previous
        while second:
            first_next, second_next = first.next, second.next
            first.next = second
            second.next = first_next
            first, second = first_next, second_next
