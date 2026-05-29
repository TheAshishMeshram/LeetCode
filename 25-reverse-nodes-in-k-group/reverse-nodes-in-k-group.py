class Solution:
    def reverseKGroup(self, head, k):

        def reverse(start, end):
            prev = end

            while start != end:
                temp = start.next
                start.next = prev
                prev = start
                start = temp

            return prev

        count = 0
        node = head

        while node and count < k:
            node = node.next
            count += 1

        if count == k:
            new_head = reverse(head, node)
            head.next = self.reverseKGroup(node, k)
            return new_head

        return head