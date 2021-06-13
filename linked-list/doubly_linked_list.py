class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    # Creation of DLL
    def create_dll(self, node_value):
        node = Node(node_value)
        node.next = None
        node.prev = None
        self.head = node
        self.tail = node
        return "The DLL is created successfully"
    

doubly_linked_list = DoublyLinkedList()
doubly_linked_list.create_dll(5)

for node in doubly_linked_list:
    print(node.value, end=" <--> ")

