from tarfile import data_filter

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    #Insert begining
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    #Print that list
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

#Example
ll = LinkedList()
ll.insert_at_beginning(10)
ll.insert_at_beginning(20)
ll.print_list() #