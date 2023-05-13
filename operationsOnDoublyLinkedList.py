class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def add_beg(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    def add_pos(self, data, index):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            node = self.head
            for _ in range(index-1):
                node = node.next
            new_node.next = node
            new_node.prev = node.prev
            node.prev.next = new_node
            node.prev = new_node

    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            node = self.head
            while node.next:
                node = node.next
            new_node.prev = node
            node.next = new_node

    def del_beg(self):
        if self.head is None:
            print("List is empty")
        else:
            self.head = self.head.next
            self.head.prev = None

    def del_pos(self, index):
        if self.head is None:
            print("List is empty")
        else:
            node = self.head
            for _ in range(index-1):
                node = node.next
            node.prev.next = node.next
            node.next.prev = node.prev

    def del_end(self):
        if self.head is None:
            print("List is empty")
        else:
            node = self.head
            while node.next:
                node = node.next
            node.prev.next = None

    def display(self):
        if self.head is None:
            print("List is empty")
        else:
            node = self.head
            while node:
                print(node.data, end=" ")
                node = node.next
            print()


dll = DoublyLinkedList()
for i in range(0, 100, 5):
    dll.add_beg(i)
dll.display()
print("Adding 200 at position 5")
dll.add_pos(200, 5)
dll.display()
print("Adding 300 at end")
dll.add_end(300)
dll.display()
print("Deleting from beginning")
dll.del_beg()
dll.display()
print("Deleting from position 5")
dll.del_pos(5)
dll.display()
print("Deleting from end")
dll.del_end()
dll.display()
