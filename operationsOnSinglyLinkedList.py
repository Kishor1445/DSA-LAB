class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def add_beg(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def add_pos(self, data, index):
        new_node = Node(data)
        node = self.head
        for _ in range(index-1):
            node = node.next
        new_node.next = node.next
        node.next = new_node

    def add_end(self, data):
        new_node = Node(data)
        node = self.head
        while node.next:
            node = node.next
        node.next = new_node

    def del_beg(self):
        self.head = self.head.next

    def del_pos(self, index):
        node = self.head
        for _ in range(index-1):
            node = node.next
        node.next = node.next.next

    def del_end(self):
        node = self.head
        while node.next.next:
            node = node.next
        node.next = None

    def display(self):
        node = self.head
        while node:
            print(node.data, end='->')
            node = node.next
        print(None)


sll = SinglyLinkedList()
for i in range(0, 100, 5):
    sll.add_beg(i)
sll.display()
sll.add_pos(100, 5)
print("After adding 100 at index 5")
sll.display()
sll.add_end(200)
print("After adding 200 at the end")
sll.display()
sll.del_beg()
print("After deleting the first element")
sll.display()
sll.del_pos(5)
print("After deleting the element at index 5")
sll.display()
sll.del_end()
print("After deleting the last element")
sll.display()
