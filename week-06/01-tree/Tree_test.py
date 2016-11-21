import unittest
from Tree import Tree


class TreeTest(unittest.TestCase):
    """docstring for TreeTest"""
    def setUp(self):
        self.tree = Tree(root=5)

    def test_tree_data(self):
        print()
        print("*** test_tree_data")
        print(self.tree.data)
        self.assertEqual(self.tree.data, 5)
        print("***end test_tree_data")
        print()

    def test_tree_string_representation(self):
        print(str(self.tree))
        self.assertEqual(str(self.tree), str(self.tree.data))

    def test_tree_children_exist(self):
        print()
        print("*** test test_tree_children_exist")
        self.tree.add_child(5, 4)
        self.tree.add_child(5, 7)
        self.tree.add_child(5, 9)
        print(self.tree.children)
        self.assertTrue(len(self.tree.children) > 0)
        print("***end test test_tree_children_exist")
        print()

    def test_has_children(self):
        print()
        print("*** has_children")
        self.tree.add_child(5, 4)
        self.tree.add_child(5, 8)
        self.tree.add_child(6, 9)
        print(self.tree.has_children())
        self.assertTrue(str(self.tree.children) == "[4, 8]")
        print("***end has_children")
        print()

    def test_find_proper_node(self):
        print()
        print("*** test_find_proper_node")
        print(self.tree.has_children())
        self.tree.add_child(5, 19)
        print(self.tree.has_children())
        print("***end test_find_proper_node")
        print()


if __name__ == "__main__":
    unittest.main()

