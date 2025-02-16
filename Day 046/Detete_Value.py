class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def delete(self, value):
        # Case 1: If the head node itself needs to be deleted
        if self.head and self.head.value == value:
            self.head = self.head.next
            return

        # Case 2: Find the node to be deleted
        prev = None
        curr = self.head
        while curr and curr.value != value:
            prev = curr
            curr = curr.next

        # If the node was not found
        if not curr:
            return

        # Case 3: Remove the node
        prev.next = curr.next

    def display(self):
        curr = self.head
        while curr:
            print(curr.value, end=" -> ")
            curr = curr.next
        print("None")

# Example Usage:
ll = SinglyLinkedList()
ll.insert(3)
ll.insert(2)
ll.insert(1)

print("Before deletion:")
ll.display()
ll.delete(2)

print("After deletion:")
ll.display()
