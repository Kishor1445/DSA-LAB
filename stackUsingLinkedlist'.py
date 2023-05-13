class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def push(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

    def pop(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            popped_node = self.head
            self.head = self.head.next
            popped_node.next = None
            return popped_node.data

    def peek(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            return self.head.data

    def display(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            node = self.head
            while node:
                print(node.data, end="->")
                node = node.next
            print("None")


s = Stack()
for i in range(0, 100, 5):
    s.push(i)
s.display()
print(s.peek())
print(s.pop())
s.display()
