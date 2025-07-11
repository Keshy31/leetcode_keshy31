from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        prev = None
        curr = head

        print_list(curr)

        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev


# Helper function to print a linked list (for debugging)
def print_list(head: Optional[ListNode]):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")


head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))

solution = Solution()
merged = solution.reverseList(head)
print_list(merged)
