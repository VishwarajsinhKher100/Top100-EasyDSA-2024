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

    # Display linked list
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

# Merge two sorted linked lists
def MergeSortedLists(l1, l2):
    dummy = Node(0)  # Dummy node to hold the merged list
    current = dummy

    while l1 is not None and l2 is not None:
        if l1.data < l2.data:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next  # Move to next node

    # Append remaining nodes if any
    current.next = l1 if l1 is not None else l2

    return dummy.next  # The merged linked list starts from dummy.next

# Example Usage
l1 = SinglyLinkedList()
l1.InsertAtEnd(1)
l1.InsertAtEnd(3)
l1.InsertAtEnd(5)

l2 = SinglyLinkedList()
l2.InsertAtEnd(2)
l2.InsertAtEnd(4)
l2.InsertAtEnd(6)

print("List 1:")
l1.display()

print("List 2:")
l2.display()

# Merging both lists
merged_head = MergeSortedLists(l1.head, l2.head)

# Display merged list
merged_list = SinglyLinkedList()
merged_list.head = merged_head
print("Merged Sorted List:")
merged_list.display()
