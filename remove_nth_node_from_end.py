# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def print_linked_list(head):
    """Iterates through the linked list and prints its values."""
    nodes = []
    current = head
    while current:
        nodes.append(str(current.val)) 
        current = current.next
    if not nodes:
        print("List is empty")
    else:
        print(" -> ".join(nodes))

node5 = ListNode(5)
node4 = ListNode(4, node5)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
head = ListNode(1, node2)
head2 = ListNode(1, node2)
def returnNthFromEnd(head, n):
    if not head or not head.next:
        print('this condition is turning out to be true')
        return None
    dummy = ListNode(0, head)
    left = dummy
    right = head
    while n > 0:
        right = right.next
        n -= 1
    while right:
        right = right.next
        left = left.next
    left.next.next = None
    return left.next

# returnNthFromEnd(head, 2)
print_linked_list(returnNthFromEnd(head, 5))



def removeNthFromEnd(head, n):
    if not head or not head.next:
        print('this condition is turning out to be true')
        return None
    dummy = ListNode(0, head)
    left = dummy
    right = head
    while n > 0:
        right = right.next
        n -= 1
    while right:
        right = right.next
        left = left.next
    left.next = left.next.next
    return dummy.next

print_linked_list(removeNthFromEnd(head2, 2))
