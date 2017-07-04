def insert(self, head, data):
    if not head:
        self.head = self.tail = Node(data)
    else:
        self.tail.next = self.tail = Node(data)
    return self.head
