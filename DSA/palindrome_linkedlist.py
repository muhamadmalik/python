# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def isPalindrome(head):
    
    stack = []
    
    
    curr = head
    
    while curr:
        stack.append(curr.val)
        curr = curr.next
    
    curr = head 
    
    while curr and curr.val == stack.pop():
        curr = curr.next
    
    return not curr



node = ListNode(1)
node.next = ListNode(2)
node.next.next = ListNode(32)
node.next.next.next = ListNode(22)
node.next.next.next.next = ListNode(1)
print(isPalindrome(node))