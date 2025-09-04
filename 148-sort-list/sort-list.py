# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        curr = head

        arr = []

        while (curr is not None):

            arr.append(curr.val)

            curr = curr.next
        
        arr.sort()

        i = 0
        curr = head

        while (curr is not None):

            curr.val = arr[i]
            curr = curr.next
            i += 1

        return head

        