import unittest
from Tree import Tree


class TreeTest(unittest.TestCase):
    """docstring for TreeTest"""
    def setUp(self):
        self.tree = Tree(root=5)

    def test_tree_data(self):
        # print()
        # print("*** test_tree_data")
        # print(self.tree.data)
        self.assertEqual(self.tree.data, 5)
        # print("***end test_tree_data")
        # print()

    def test_tree_string_representation(self):
        # print(str(self.tree))
        self.assertEqual(str(self.tree), str(self.tree.data))

    def test_tree_children_exist(self):
        # print()
        # print("*** test test_tree_children_exist")
        self.tree.add_child(5, 4)
        self.tree.add_child(5, 7)
        self.tree.add_child(5, 9)
        # print(self.tree.children)
        self.assertTrue(len(self.tree.children) > 0)
        # print("***end test test_tree_children_exist")
        # print()

    def test_has_children(self):
        # print()
        # print("*** has_children")
        self.tree.add_child(5, 4)
        self.tree.add_child(5, 8)
        self.tree.add_child(6, 9)
        # print(self.tree.has_children())
        self.assertTrue(str(self.tree.children) == "[4, 8]")
        # print("***end has_children")
        # print()

    def test_find_proper_node(self):
        # print()
        # print("*** test_find_proper_node")
        # print(self.tree.has_children())
        self.assertFalse(self.tree.find_proper_node(9, 6))
        self.tree.add_child(5, 19)
        # print(self.tree.has_children())
        # print("***end test_find_proper_node")
        # print()

    def test_find_proper_node_when_children(self):
        # print()
        # print("*** test_find_proper_node_when_children")
        self.tree.add_child(5, 4)
        self.tree.add_child(5, 8)
        self.tree.add_child(5, 9)
        # add children to the children
        self.tree.add_child(8, 7)
        self.tree.add_child(8, 3)
        self.tree.add_child(8, 45)

        self.tree.add_child(9, 62)
        self.tree.add_child(9, 68)
        self.tree.add_child(9, 93)

        self.tree.add_child(4, 41)
        self.tree.add_child(4, 42)
        self.tree.add_child(4, 43)
        self.tree.add_child(4, 44)

        # print(self.tree.children[1].children)
        # print(self.tree.children[2].children)
        # print(self.tree.children[0].children)

        self.assertEqual(str(self.tree.children[1].children), "[7, 3, 45]")
        self.assertEqual(str(self.tree.children[2].children), "[62, 68, 93]")
        self.assertEqual(
            str(self.tree.children[0].children), "[41, 42, 43, 44]")
        # print("***end test_find_proper_node_when_children")

    def test_find(self):
        # print()
        # print("*** test_find")
        self.tree.add_child(5, 4)
        self.tree.add_child(5, 8)
        self.tree.add_child(5, 9)
        # print(self.tree.find(5))
        self.assertEqual(self.tree.find(5), True)
        self.assertEqual(self.tree.find(6), False)

        self.tree.add_child(4, 41)
        self.tree.add_child(4, 42)
        self.tree.add_child(4, 43)
        self.tree.add_child(4, 44)

        self.tree.add_child(8, 82)
        self.tree.add_child(8, 87)
        self.tree.add_child(8, 83)

        self.tree.add_child(9, 92)
        self.tree.add_child(9, 98)
        self.tree.add_child(9, 93)

        # print(self.tree.find(4))
        # print(self.tree.find(8))
        # print(self.tree.find(9))
        # print(self.tree.find(41))
        # print(self.tree.find(42))
        # print(self.tree.find(43))
        # print(self.tree.find(44))
        # print(self.tree.find(82))
        # print(self.tree.find(87))
        # print(self.tree.find(83))
        # print(self.tree.find(92))
        # print(self.tree.find(98))
        # print(self.tree.find(93))
        self.assertEqual(self.tree.find(4), True)
        self.assertEqual(self.tree.find(8), True)
        self.assertEqual(self.tree.find(9), True)
        self.assertEqual(self.tree.find(41), True)
        self.assertEqual(self.tree.find(42), True)
        self.assertEqual(self.tree.find(43), True)
        self.assertEqual(self.tree.find(44), True)
        self.assertEqual(self.tree.find(82), True)
        self.assertEqual(self.tree.find(87), True)
        self.assertEqual(self.tree.find(83), True)
        self.assertEqual(self.tree.find(92), True)
        self.assertEqual(self.tree.find(98), True)
        self.assertEqual(self.tree.find(93), True)

        # print(self.tree.find(28))
        # print(self.tree.find(13))
        # print(self.tree.find(87))
        # print(self.tree.find(46))
        self.assertEqual(self.tree.find(28), False)
        self.assertEqual(self.tree.find(13), False)
        self.assertEqual(self.tree.find(87), True)
        self.assertEqual(self.tree.find(46), False)

        # print("***end test_find")
        # print()

    def test_height(self):
        # print()
        # print("*** test_height")
        # self.assertEqual(self.tree.height(), 1)

        # test when only root
        self.assertEqual(self.tree.height(), 1)

        # test when tree is with greater height than 1
        self.tree.add_child(5, 4)
        self.tree.add_child(5, 8)
        self.tree.add_child(5, 9)
        self.tree.add_child(4, 41)
        self.tree.add_child(4, 42)
        self.tree.add_child(4, 43)
        self.tree.add_child(4, 44)
        self.tree.add_child(44, 441)
        self.tree.add_child(44, 442)
        self.tree.add_child(44, 443)
        self.tree.add_child(443, "a")
        self.tree.add_child(443, "b")
        self.tree.add_child(443, "c")
        self.assertEqual(self.tree.height(), 5)

        self.tree.children = []

        # test after we have reset the tree's children to []
        self.assertEqual(self.tree.height(), 1)
        self.tree.add_child(5, 8)
        self.assertEqual(self.tree.height(), 2)
        self.tree.add_child(8, 14)
        self.assertEqual(self.tree.height(), 3)
        self.tree.add_child(14, 62)
        self.assertEqual(self.tree.height(), 4)

        # print("***end test_height")
        # print()

    def test_attr_count(self):
        self.tree.add_child(5, 4)
        self.tree.add_child(5, 8)
        self.tree.add_child(5, 9)
        self.tree.add_child(4, 41)
        self.tree.add_child(4, 42)
        self.tree.add_child(4, 43)
        self.tree.add_child(4, 44)
        self.tree.add_child(8, 82)
        self.tree.add_child(8, 87)
        self.tree.add_child(8, 83)
        self.tree.add_child(9, 92)
        self.tree.add_child(9, 98)
        self.tree.add_child(9, 93)

        self.assertEqual(self.tree.count_nodes(), 14)


if __name__ == "__main__":
    unittest.main()

