# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack=[]
        current=head
        while current:
            stack.append(current.val)
            current=current.next
        newCurrent=head
        while newCurrent:
            if newCurrent.val!=stack.pop():
                return False
            newCurrent=newCurrent.next
        return True
    
            
            
        