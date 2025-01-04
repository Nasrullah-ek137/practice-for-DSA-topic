# stack implementing by using list..

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, data):
        self.items.append(data)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()  # Corrected this condition
        else:
            raise IndexError("Stack is Empty")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]  # Corrected this condition
        else:
            raise IndexError("Stack is Empty")

    def size(self):
        return len(self.items)


# Example usage:
s = Stack()
s.push(10)
s.push(20)
s.push(30)

print(s.pop())  # Outputs 30
print(s.peek()) # Outputs 20
print(s.size()) # Outputs 2
