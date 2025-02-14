class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    # Insert at the end
    def InsertAtEnd(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return
        
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    # Find the middle node using slow and fast pointers
    def FindMiddle(self):
        slow = self.head
        fast = self.head

        while fast is not None and fast.next is not None:
            slow = slow.next  # Move one step
            fast = fast.next.next  # Move two steps

        return slow.data if slow else None  # Return middle node data

    # Display linked list
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

# Example Usage
ll = SinglyLinkedList()
ll.InsertAtEnd(10)
ll.InsertAtEnd(20)
ll.InsertAtEnd(30)
ll.InsertAtEnd(40)
ll.InsertAtEnd(50)

ll.display()  
print("Middle element:", ll.FindMiddle())  

ll.InsertAtEnd(60)
ll.display()
print("Middle element:", ll.FindMiddle())
