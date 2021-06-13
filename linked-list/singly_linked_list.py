class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    
    def insert(self, value, location=-11):
        """
        Insert a node with a value to a specific position.
        * Time complexity: O(n)
        * Space complexity: O(1)
        """
        new_node = Node(value)
        # when our SLL is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            # inserting at begining
            if location == 0:
                new_node.next = self.head
                self.head = new_node
            # insertion at end
            elif location == -1:
                new_node.next = None
                self.tail.next = new_node
                self.tail = new_node
            # anywhere at the middle
            else:                               # 1.-->2.-->(3)-->4-->5; location = 2
                temp_node = self.head
                index = 0
                while index < location - 1: # index = 0
                    temp_node = temp_node.next
                    index += 1
                # method - 1
                # next_node = temp_node.next
                # temp_node.next = new_node
                # new_node.next = next_node
                
                # method - 2
                new_node.next = temp_node.next
                temp_node.next = new_node

sample_list = SinglyLinkedList()
sample_list.insert(3)
sample_list.insert(0, 0)
sample_list.insert(1, 1)
sample_list.insert(5, -1)
sample_list.insert(2, 2)
sample_list.insert(4, 4)
sample_list.insert(6, -1)
# print([node.value for node in sample_list])
for node in sample_list:
    print(node.value, end="-->")
