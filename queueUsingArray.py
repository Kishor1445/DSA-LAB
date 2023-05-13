class Queue:
    def __init__(self):
        self.__arr = []

    def enqueue(self, data):
        self.__arr.append(data)

    def dequeue(self):
        return self.__arr.pop(0)

    def peek(self):
        return self.__arr[0]

    def is_empty(self):
        return len(self.__arr) == 0

    def display(self):
        for i in self.__arr:
            print(i, end=" ")
        print()

    def size(self):
        return len(self.__arr)


q = Queue()
for i in range(1, 110, 5):
    q.enqueue(i)
q.display()
print(q.size())
print(q.peek())
print(q.dequeue())
print(q.peek())
print(q.is_empty())
q.display()
