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
    #     size = self.ll.size()
    #     self.ll.remove(0)
    #     size2 = self.ll.size()
    #     self.assertFalse(size == size2)


if __name__ == '__main__':
    unittest.main()