class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def append(self, value)->bool:
        new_node = Node(value)
        if self.head == None:
            self.head.next = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def prepend(self, value)->bool:
        if self.head == None:
            return self.append(value)
        else:
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node
            self.length += 1
        return True
    
    def find(self, value)->int:
        current_node = self.head
        index = 0
        while current_node:
            if current_node.value == value:
                return index
            current_node = current_node.next
            index += 1
        return None
    
    def get(self, index)->Node:
        if index < 0 or index >= self.length:
            return None
        current_node = self.head
        for _ in range(index):
            current_node = current_node.next
        return current_node
    
    def set_node(self, value, index)->bool:
        current_node = self.get(index)
        if current_node:
            current_node.value = value
            return True
        return False

    def insert(self, value, index)->bool:
        if index < 0 or index > self.length:
            return False
        if index == self.length:
            return self.append(value)
        if index == 0:
            return self.prepend(value)
        new_node = Node(value)
        leader = self.get(index-1)
        new_node.next = leader.next
        leader.next = new_node
        self.length += 1
        return True
    
    def remove(self, index)->Node:
        if index < 0 or index >= self.length:
            return None
        elif index == 0:
            return self.pop_first()
        elif index == self.length-1:
            return self.pop()
        current_node = self.get(index-1)
        temp = current_node.next
        current_node.next = temp.next
        self.length -= 1
        return temp

    def pop(self)->Node:
        current_node = self.head
        while current_node:
            if current_node.next == self.tail:
                temp = current_node.next
                current_node.next = None
                self.tail = current_node
                self.length -= 1
                return temp
            elif current_node is self.tail:
                self.head = None
                self.tail = None
                self.length -= 1
                return current_node
            current_node = current_node.next
        return None

    def pop_first(self)->Node:
        if self.length == 0:
            return None
        elif self.length == 1:
            temp = self.head
            self.head = None
            self.tail = None
        else:
            temp = self.head
            self.head = self.head.next
        self.length -= 1
        temp.next = None
        return temp

    def reverse(self)->None:
        if self.length == 0:
            return None
        elif self.length == 1:
            return self.head
        first = self.head
        second = first.next
        self.tail = self.head
        while second:
            temp = second.next
            second.next = first
            first = second
            second = temp
        self.head.next = None
        self.head = first


    def print_list(self)->None:
        current_node = self.head
        print("Linked List elements: ", end="")
        while current_node:
            print(current_node.value, end=" -> ")
            current_node = current_node.next
        print("None")

# Creating a linked list
my_linked_list = LinkedList(1)

# Operations on Linked List
my_linked_list.print_list()
print("Inserting 2 at index 2")
my_linked_list.insert(2, 2) 
my_linked_list.print_list()
print("Prepending 0")
my_linked_list.prepend(0)
my_linked_list.print_list()
print("Appending 4")
my_linked_list.append(4)
my_linked_list.print_list()
print("Inserting 3 at index 3")
my_linked_list.insert(3, 3)
my_linked_list.print_list()
print("Reversing linked list")
my_linked_list.reverse()
my_linked_list.print_list()
print("Popping first element")
my_linked_list.pop_first()
my_linked_list.print_list()
print("Index of 2: {}".format(my_linked_list.find(2)))
print("Length of linked list: ", my_linked_list.length)
print("Element at index 1: ", my_linked_list.get(1))

# Popping elements
print("Popped element: ", my_linked_list.pop())
print("Popped element: ", my_linked_list.pop_first())
print("Popped element: ", my_linked_list.pop())
print("Popped element: ", my_linked_list.pop_first())
print("Popped element: ", my_linked_list.pop())
print("Popped element: ", my_linked_list.pop_first())
my_linked_list.print_list()