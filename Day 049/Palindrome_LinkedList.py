class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def is_palindrome(head):
    if not head or not head.next:
        return True

    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    prev = None
    while slow:
        temp = slow.next
        slow.next = prev
        prev = slow
        slow = temp

    left, right = head, prev
    while right: 
        if left.val != right.val:
            return False
        left = left.next
        right = right.next

    return True

head = Node(1)
head.next = Node(2)
head.next.next = Node(2)
head.next.next.next = Node(1)

print(is_palindrome(head))
