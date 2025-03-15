# We have Head and Tail pointers to the linked list
# We have a Node class to create nodes
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None  # type: Node | None

# We have a linked_list class to create linked lists
class linked_list:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_node(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def print_list(self):
        current_node = self.head
        while current_node != None:
            print(current_node.value)
            current_node = current_node.next