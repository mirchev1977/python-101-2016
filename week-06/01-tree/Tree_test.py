import unittest
from Tree import Tree


class TreeTest(unittest.TestCase):
    """docstring for TreeTest"""
    def setUp(self):
        self.tree = Tree(root=5)

    def test_tree_data(self):
        print(self.tree.data)
        self.assertEqual(self.tree.data, 5)

    def test_tree_string_representation(self):
        print(str(self.tree))
        self.assertEqual(str(self.tree), str(self.tree.data))


    def test_tree_children_exist(self):
        self.tree.add_child(5, 4)
        self.tree.add_child(5, 7)
        self.tree.add_child(5, 9)
        print(self.tree.children)
        self.assertTrue(len(self.tree.children) > 0)


if __name__ == "__main__":
    unittest.main()

