from node import Node


class LinkedList:
    def __init__(self):
        self.current_node = Node(None, None)
        self.__size = 0

    def add_element(self, data):
        self.__size += 1
        node = Node(data, self)
        self.current_node.next(node)

    def index(self, index):
        pass

    def size(self):
        return self.__size

    def remove(self, index):
        pass

    def pprint(self):
        pass

    def to_list(self):
        pass

    def add_at_index(self, index, data):
        pass

    def add_first(self, data):
        pass

    def add_list(self, list: "list"):
        pass

    # def add_linked_list(self, Linkedlist: LinkedList):
    #     pass

    def ll_from_to(self, start_index, end_index):
        pass

    def pop(self):
        pass

    def reduce_to_unique(self):
        pass
