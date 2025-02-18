class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def find_nth_from_end(head: Node, n: int) -> Node:
    first = second = head

    # Move first pointer n steps ahead
    for _ in range(n):
        if first is None:  # Edge case: If n is greater than the length of the list
            return None
        first = first.next

    # Move both pointers until first reaches the end
    while first:
        first = first.next
        second = second.next

    return second  # Second is now at the nth node from the end

# Example Usage:
def print_nth_from_end(head, n):
    node = find_nth_from_end(head, n)
    if node:
        print(f"{n}th node from the end is: {node.val}")
    else:
        print("List is too short!")

# Creating a linked list: 1 -> 2 -> 3 -> 4 -> 5
head = Node(1, Node(2, Node(3, Node(4, Node(5)))))

# Test cases
print_nth_from_end(head, 2)  
print_nth_from_end(head, 5)  
print_nth_from_end(head, 6) 
