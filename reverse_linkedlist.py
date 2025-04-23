from typing import Optional, List

# Definition for singly-linked list (Assume this is provided)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    # Optional: For easier visualization
    def __repr__(self):
        vals = []
        curr = self
        while curr:
            vals.append(str(curr.val))
            curr = curr.next
        return " -> ".join(vals) if vals else "None"


# --- Helper Functions (Minimal) ---
def create_linked_list(values: List[int]) -> Optional[ListNode]:
    if not values: return None
    head = ListNode(values[0])
    curr = head
    for val in values[1:]: curr.next = ListNode(val); curr = curr.next
    return head

def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    vals = []; curr = head
    while curr: vals.append(curr.val); curr = curr.next
    return vals

def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head: 
        return None
    newHead = head
    if head.next:
        newHead = reverseList(head.next)
        head.next.next = head
        pass
    head.next = None
    return newHead


head1 = create_linked_list([1, 2, 3, 4])
print(f"Original: {head1}")
reversed_head1 = reverseList(head1)
result1 = linked_list_to_list(reversed_head1)
print(f"Reversed: {reversed_head1}")

