



# create a class for node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Create a class for the linkedList
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def remove(self, data):
        current = self.head
        previous = None

        if current and current.data == data:
            self.head = current.next
            current = None
            return

        while current and current.data != data:
            previous = current
            current = current.next

        if not current:
            print("Node not found in the LinkedList!")
            return

        previous.next = current.next
        current = None

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

linked_list = LinkedList()
linked_list.append(10)
linked_list.append(20)
linked_list.append(30)
linked_list.append(50)
linked_list.append(60)
linked_list.append(70)

linked_list.remove(40)
linked_list.print_list()

