import unittest
from cell import Cell
from matrix import Matrix


class TestMatrix(unittest.TestCase):
    def setUp(self):
        self.matrix = Matrix()

    def test_find_matrix_dimensions(self):
        self.matrix.coord_list = [2, 8, 3, 4, 9, 11, 3, 1, 6]
        self.assertEqual(self.matrix.find_matrix_dimensions(), 11)
        self.matrix.coord_list = [2, 8, 3, 44, 9, 11, 3, 1, 6]
        self.assertEqual(self.matrix.find_matrix_dimensions(), 44)

    def test_fill_matrix_with_dead(self):

        test_matrix = [[Cell(0, 1), Cell(0, 2), Cell(0, 3), Cell(0, 4)],
                       [Cell(1, 1), Cell(1, 2), Cell(1, 3), Cell(1, 4)],
                       [Cell(2, 1), Cell(2, 2), Cell(2, 3), Cell(2, 4)],
                       [Cell(3, 1), Cell(3, 2), Cell(3, 3), Cell(3, 4)]]

        self.matrix.fill_matrix_with_dead(2)
        first_row = self.matrix.matrix[0]
        self.assertEqual(len(self.matrix.matrix), len(test_matrix))
        self.assertEqual(len(self.matrix.matrix[0]), len(first_row))
        self.assertEqual(self.matrix.matrix[0][0], first_row[0])
        self.assertEqual(self.matrix.matrix[0][0].isAlive, False)


if __name__ == '__main__':
    unittest.main()
