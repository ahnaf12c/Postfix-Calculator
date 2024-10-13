class Stack:
    def __init__(self):
        self.stack = []

    # Function to push an element onto the stack
    def push(self, value):
        if isinstance(value, (int, float)):  # Check if the value is an integer or float
            self.stack.append(value)
            #print(f"Pushed {value} onto the stack")
        else:
            print("Only numerical values (int or float) are allowed.")

    # Function to pop an element from the stack
    def pop(self):
        if not self.is_empty():
            value = self.stack.pop()
            #print(f"Popped {value} from the stack")
            return value
        else:
            print("Stack is empty!")
            return None

    # Function to pop an element at a specific index
    def pop_at_index(self, index):
        if index < len(self.stack):
            value = self.stack.pop(index)
            #print(f"Popped {value} from index {index} of the stack")
            return value
        else:
            print("Index out of range!")
            return None

    # Function to get the top element of the stack without popping
    def get_top(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("Stack is empty!")
            return None

    # Function to get the second top element of the stack without popping
    def get_second_top(self):
        if len(self.stack) >= 2:
            return self.stack[-2]
        else:
            print("Stack doesn't have enough elements for a second top!")
            return None

    # Function to check if the stack is empty
    def is_empty(self):
        return len(self.stack) == 0

    # Function to display the current stack
    def display(self):
        if not self.is_empty():
            print(self.stack)
        else:
            print("VOID")

if __name__ ==  '__main__':
    # Example usage
    stack = Stack()

    # Push elements onto the stack
    stack.push(10)
    stack.push(20.5)
    stack.push(15)
    stack.push(30)

    # Display the current stack
    stack.display()

    # Pop element at index 1
    stack.pop_at_index(1)

    # Display the stack after popping at index
    stack.display()

    # Pop element at an invalid index (e.g., 10)
    stack.pop_at_index(10)
