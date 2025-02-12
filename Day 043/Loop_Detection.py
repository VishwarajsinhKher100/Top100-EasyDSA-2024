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

    # Detect loop using Floyd’s Cycle Detection Algorithm
    def DetectLoop(self):
        slow = self.head
        fast = self.head

        while fast is not None and fast.next is not None:
            slow = slow.next  # Move slow pointer one step
            fast = fast.next.next  # Move fast pointer two steps

            if slow == fast:  # If they meet, loop exists
                return True
        
        return False  # No loop detected

    # Create a loop for testing
    def CreateLoop(self, position):
        if position < 1:
            return
        
        loop_start_node = None
        temp = self.head
        count = 1

        while temp and temp.next:
            if count == position:
                loop_start_node = temp  # Mark the loop start
            temp = temp.next
            count += 1
        
        if temp:
            temp.next = loop_start_node  # Create the loop

# Example Usage
ll = SinglyLinkedList()
ll.InsertAtEnd(10)
ll.InsertAtEnd(20)
ll.InsertAtEnd(30)
ll.InsertAtEnd(40)
ll.InsertAtEnd(50)

ll.CreateLoop(2)  # Creating a loop at position 2

if ll.DetectLoop():
    print("Loop detected in the linked list")
else:
    print("No loop detected")
