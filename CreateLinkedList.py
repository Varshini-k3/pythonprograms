class Node:
    """Represents a single node in the linked list."""
    def __init__(self, data):
        self.data = data  # Stores the actual value
        self.next = None  # Points to the next node, defaults to None


class LinkedList:
    """Manages the nodes and structural operations of the list."""
    def __init__(self):
        self.head = None  # The first node in the list

    def append(self, data):
        """Adds a new node containing the data to the end of the list."""
        new_node = Node(data)
        
        # If the list is empty, make the new node the head
        if not self.head:
            self.head = new_node
            return
        
        # Otherwise, traverse to the last node
        current = self.head
        while current.next:
            current = current.next
            
        # Point the last node's next pointer to the new node
        current.next = new_node

    def display(self):
        """Prints the entire linked list structure."""
        if not self.head:
            print("Empty List")
            return
            
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# --- Demonstration ---
if __name__ == "__main__":
    # Initialize the linked list
    my_list = LinkedList()

    # Append elements
    my_list.append(10)
    my_list.append(20)
    my_list.append(30)

    # Display the list
    print("Linked List Elements:")
    my_list.display()
