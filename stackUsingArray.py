class Stack:
    def __init__(self, size):
        self._size = size
        self._stack = []

    def is_empty(self):
        return self._stack == []

    def push(self, data):
        if len(self._stack) < self._size:
            self._stack.append(data)
        else:
            print("Stack is full")

    def pop(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            return self._stack.pop()

    def peek(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            return self._stack[-1]

    def display(self):
        print(self._stack)


s = Stack(5)
for i in [1, 5, 3, 32, 2]:
    s.push(i)
s.display()
print(s.peek())
print(s.pop())
s.display()
