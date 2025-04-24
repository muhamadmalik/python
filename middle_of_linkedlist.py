class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

node5 = ListNode(5)
node4 = ListNode(4, node5)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
head = ListNode(1, node2) 

def middleNode(head):
    fast = head
    slow = head

    while fast and fast.next:
        slow = slow.next        
        fast = fast.next.next   
    print(slow)
    return slow

result_node = middleNode(head)
