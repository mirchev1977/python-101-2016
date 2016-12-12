import unittest
from Node import Node
from Tree import Tree


class TestTree(unittest.TestCase):
    """docstring """

    def test_property_node(self):
        node = Node(">>>-<<<", None)
        self.tree = Tree(">>>-<<<")
        self.assertEqual(self.tree.node.root,
                         ['>', '>', '>', '-', '<', '<', '<'])

    def test_solve(self):
        self.tree = Tree(">>>_<<<")
        self.tree.solve()


if __name__ == "__main__":
    unittest.main()
