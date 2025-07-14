class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        result = 0
        current = head
        while current:
            result = (result << 1) | current.val  # Left shift and add current digit
            current = current.next
        return result
