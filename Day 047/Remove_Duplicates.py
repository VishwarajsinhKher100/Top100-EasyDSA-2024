class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

def remove_duplicates(head):
    if not head:
        return None

    seen = set()
    current = head
    seen.add(current.data)

    while current.next:
        if current.next.data in seen:
            current.next = current.next.next  # Skip duplicate node
        else:
            seen.add(current.next.data)
            current = current.next  # Move forward

    return head

# Helper function to print linked list
def print_list(head):
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("None")

# Example usage
head = Node(1, Node(2, Node(2, Node(3, Node(4, Node(4))))))
print_list(remove_duplicates(head))
