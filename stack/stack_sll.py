class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        curr_node = self.head
        while curr_node:
            yield curr_node
            curr_node = curr_node.next 


class Stack: 
    def __init__(self):
        # self.top = None
        self.linked_list = LinkedList()

    def __str__(self):
        values = [str(x.value) for x in self.linked_list]
        return "\n".join(values)

    def is_empty(self):
        if self.linked_list.head == None:
            return True
        else:
            return False
    
    def push(self, value):
        node = Node(value)
        node.next = self.linked_list.head
        self.linked_list.head = node
    
    def pop(self):
        if self.is_empty():
            return "Stack is already empty!"
        else:
            node_value = self.linked_list.head.value
            self.linked_list.head = self.linked_list.head.next
            return node_value

    def peek(self):
        if self.is_empty():
            return "Stack is already empty!"
        else:
            node_value = self.linked_list.head.value
            return node_value

    def delete(self):
        self.linked_list.head = None


custom_stack = Stack()

custom_stack.push(1)
custom_stack.push(2)
custom_stack.push(3)
custom_stack.push(5)

print("------------")
print(custom_stack)
custom_stack.pop()

print("------------")
print(custom_stack)
custom_stack.pop()

print("------------")
print(custom_stack)

print("Peeking: ", custom_stack.peek())
custom_stack.delete()

print(custom_stack.is_empty())
