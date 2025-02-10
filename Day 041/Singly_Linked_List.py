class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    # Insert at the beginning
    def InsertAtBeginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insert at the end
    def InsertAtEnd(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node
    
    # Insert at the specific position
    def InsertAtPosition(self, position, data):
        if position < 1:
            print("Invalid position!")
            return
        
        new_node = Node(data)
        if position == 1:
            new_node.next = self.head
            self.head = new_node
            return

        prev = self.head
        count = 1
        while count < position - 1 and prev is not None:
            prev = prev.next
            count += 1

        if prev is None:
            print("Invalid position!")
            return

        new_node.next = prev.next
        prev.next = new_node

    # Delete at the beginning
    def DeleteAtBeginning(self):
        if not self.head:
            return
        self.head = self.head.next

    # Delete at the end
    def DeleteAtEnd(self):
        if self.head is None:
            return

        if self.head.next is None:
            self.head = None
            return

        second_last = self.head
        while second_last.next and second_last.next.next:
            second_last = second_last.next

        second_last.next = None
    
    # Delete at the specific position
    def DeleteAtPosition(self, position):
        if self.head is None or position < 1:
            return

        if position == 1:
            self.head = self.head.next
            return

        current = self.head
        prev = None
        for _ in range(position - 1):
            if current is None:
                return
            prev = current
            current = current.next

        if current is None:
            return

        prev.next = current.next

    # Display the linked list
    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example Usage
ll = SinglyLinkedList()
ll.InsertAtEnd(10)
ll.InsertAtEnd(20)
ll.InsertAtEnd(30)
ll.InsertAtBeginning(40)
ll.InsertAtBeginning(50)
ll.InsertAtEnd(60)
ll.display()

ll.DeleteAtPosition(1)
ll.DeleteAtBeginning()
ll.DeleteAtEnd()
ll.display()