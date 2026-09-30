import heapq


class Solution:
    def mergeKLists(self, lists):
        heap = []
        for index, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, index, node))

        dummy = current = ListNode()
        while heap:
            _, index, node = heapq.heappop(heap)
            current.next = node
            current = current.next

            if node.next:
                heapq.heappush(heap, (node.next.val, index, node.next))

        return dummy.next
