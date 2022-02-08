
class Node:

    def __init__(self, value):

        self.value = value

        self.next = None

        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None



    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            print("Head Node created:", self.head.value)
            return
        node = self.head
        while node.next is not None:
            node = node.next
        node.next = new_node
        print("Appended new Node with value:", node.next.value)

    def prepend(self, value):
        new_object = Node(value)
        if self.head is None:
            self.head = new_object
            self.tail = new_object
            print("Head Node created:", self.head.value)
            return



        new_object.next = self.head

        self.head.prev = new_object

        self.head = new_object

        print("Prepended new object with value:", self.head.value)

        print("Node following Head is:", self.head.next.value)





llist = LinkedList()