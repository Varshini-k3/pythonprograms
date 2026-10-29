from collections import deque

def manage_deque():
    # 1. Initialize an empty double-ended queue
    dq = deque()
    
    # 2. Add elements to both ends
    dq.append("Middle")        # Adds to the right end
    dq.append("Right_End")     # Adds to the right end
    dq.appendleft("Left_End")  # Adds to the left end
    
    # 3. Print the entire deque structure
    print("Initial Deque:")
    print(dq)
    print("-" * 30)

    # 4. Read / Access specific elements without removing them
    print("Reading elements:")
    print(f"Front element (Index 0):  {dq[0]}")
    print(f"Back element (Index -1): {dq[-1]}")
    print("-" * 30)

    # 5. Remove elements from both ends (and print them)
    print("Removing elements:")
    left_item = dq.popleft()   # Removes from the front
    right_item = dq.pop()      # Removes from the back
    print(f"Removed from left:  {left_item}")
    print(f"Removed from right: {right_item}")
    print("-" * 30)

    # 6. Print the remaining elements
    print("Final Deque content:")
    print(list(dq))  # Casted to list for clean printing

if __name__ == "__main__":
    manage_deque()
