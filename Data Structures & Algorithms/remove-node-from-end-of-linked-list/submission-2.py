# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Create a dummy node to cleanly handle deleting the head node
        dummy = ListNode(0, head)
        fast = dummy
        slow = dummy
        
        # 1. Advance fast pointer so there is a gap of n nodes between fast and slow
        for _ in range(n + 1):
            fast = fast.next
            
        # 2. Move both pointers together until fast reaches the end
        while fast:
            fast = fast.next
            slow = slow.next
            
        # 3. Skip the target node
        slow.next = slow.next.next
        
        # Return the actual head of the list
        return dummy.next
