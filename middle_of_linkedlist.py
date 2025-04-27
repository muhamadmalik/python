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

print("Original list:")
# print_linked_list(head) 

def deleteMiddleNode(head):
    if not head or not head.next:
        return None 

    dummy = ListNode(next=head) 
    fast = head
    slow = dummy

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    print_linked_list(slow)
    slow.next = slow.next.next

    return dummy.next

result_head = deleteMiddleNode(head)

print("\nList after deleting middle node:")
print_linked_list(result_head) 