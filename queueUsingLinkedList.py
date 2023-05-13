class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.front = self.rear = None

    def is_empty(self):
        return self.front is None

    def peek(self):
        if self.is_empty():
            return None
        return self.front.value

    def enqueue(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            return None
        node = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return node.value

    def display(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            node = self.front
            while node:
                print(node.value, end=" ")
                node = node.next
            print()

    def size(self):
        count = 0
        node = self.front
        while node:
            count += 1
            node = node.next
        return count


q = Queue()
for i in range(0, 100, 5):
    q.enqueue(i)
q.display()
print(q.size())
print(q.peek())
print(q.dequeue())
print(q.dequeue())
q.display()