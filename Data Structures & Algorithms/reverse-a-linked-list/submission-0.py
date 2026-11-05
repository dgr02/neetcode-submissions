# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return None
            
        reverse = []

        current = head
        while current:
            reverse.append(current.val)
            current = current.next
        
        reverse.reverse()
        
        new_head = ListNode(reverse[0])
        current = new_head

        for value in reverse[1:]:
            current.next = ListNode(value)
            current = current.next
        
        return new_head
            





        