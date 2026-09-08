# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # prev = None
        # curr = head
        # while curr:
        #     forward = curr.next
        #     curr.next = prev
        #     prev = curr 
        #     curr = forward
        # return prev

        temp = head
        prev = None

        while head:
            curr = temp.next
            temp.next = prev
            head = curr
            prev = temp
            temp = head
        return prev