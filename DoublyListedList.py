class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Pointer to the next node
        self.prev = None  # Pointer to the previous node

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Method to insert a new node at the end of the list
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        last = self.head
        while last.next:
            last = last.next
            
        last.next = new_node
        new_node.prev = last

    # Method to print the list from front to back
    def print_forward(self):
        if not self.head:
            print("The list is empty.")
            return
        
        current = self.head
        print("Traversal in forward direction:")
        while current:
            print(current.data, end=" <-> " if current.next else "\n")
            current = current.next

    # Method to print the list from back to front
    def print_backward(self):
        if not self.head:
            print("The list is empty.")
            return
        
        # 1. Navigate to the last node
        last = self.head
        while last.next:
            last = last.next
            
        # 2. Traverse backward using the prev pointer
        print("Traversal in backward direction:")
        current = last
        while current:
            print(current.data, end=" <-> " if current.prev else "\n")
            current = current.prev

# --- Execution Example ---
if __name__ == "__main__":
    dll = DoublyLinkedList()
    
    # Adding elements
    dll.append(10)
    dll.append(20)
    dll.append(30)
    dll.append(40)
    
    # Printing the list
    dll.print_forward()
    dll.print_backward()
