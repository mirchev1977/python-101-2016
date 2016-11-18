import unittest
from linked_list import LinkedList


class LinkedListTest(unittest.TestCase):

    def setUp(self):
        self.ll = LinkedList()

    def test_adding_element(self):
        self.ll.add_element(4)
        self.assertEqual(self.ll.size(), 1)
        self.ll.add_element(7)
        self.assertEqual(self.ll.size(), 2)
        self.ll.add_element(9)
        self.assertEqual(self.ll.size(), 3)

    # def test_remove_element(self):
    #     self.ll.add_element(4)
    #     self.ll.add_element(8)
    #     size = self.ll.size()
    #     self.ll.remove(0)
    #     size2 = self.ll.size()
    #     print("***print linked list size", size, size2, "****")
    #     self.assertFalse(size == size2)

    def test_print_all_elements_in_list(self):
        self.ll.add_element(4)
        self.ll.add_element(7)
        self.ll.add_element(9)
        self.ll.add_element(12)
        self.ll.add_element(45)
        node = self.ll.current_node
        while node:
            print("me: " + str(node),
                  "my_data: " + str(node.data), "next: " + str(node.next))
            node = node.next


if __name__ == '__main__':
    unittest.main()
