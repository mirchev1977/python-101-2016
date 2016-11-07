from cell import Cell


class Matrix:
    def __init__(self):
        self.living_cells = []
        self.coord_list = []
        self.matrix = []

    def input_living_cells(self):
        inp = input("Insert number of cells")
        print()
        for i in range(int(inp)):
            coord = input("Insert cell coordinates")
            coord = coord.split(" ")
            self.coord_list.append(int(coord[0]))
            self.coord_list.append(int(coord[1]))
            cell = Cell(int(coord[0]), int(coord[1]), True)

            self.living_cells.append(cell)

    def find_matrix_dimensions(self):
        greatest = max(self.coord_list)
        return greatest

    def fill_matrix_with_dead(self, width):
        for row in range(width * 2):
            row_list = []
            for col in range(width * 2):
                cell = Cell(row, col)
                row_list.append(cell)
            self.matrix.append(row_list)

    def fill_matrix_with_living(self):
        for cell in self.living_cells:
            current = self.matrix[cell.row][cell.col]
            current.isAlive = True

    def print_matrix(self):
        for row in range(len(self.matrix)):
            row_buff = ''
            for col in range(len(self.matrix)):
                current = self.matrix[row][col]
                if current.isAlive is False:
                    row_buff += '0'
                else:
                    row_buff += '*'
            print(row_buff)

    def iterate_over_matrix(self):
        for row in range(len(self.matrix)):
            for col in range(len(self.matrix)):
                current = self.matrix[row][col]
                self.check_neighbors(current)

    def check_neighbors(self, cell):
        neighbors = ((-1, -1), (-1, 0), (-1, 1),
                     (0, -1), (0, 1),
                     (1, -1), (1, 0), (1, 1))
        count_valid = 0
        for neighbor in neighbors:
            is_valid = self.neighbor_is_valid(neighbor, cell)
            if is_valid:
                count_valid += 1

        print(count_valid, cell.row, cell.col)

    def neighbor_is_valid(self, neighbor, cell):
        if cell.row + int(neighbor[0] >= 0 and
                          cell.row + int(neighbor[0]) <=
                          len(self.matrix) - 1 and
                          cell.col + int(neighbor[1]) >= 0 and
                          cell.col + int(neighbor[1]) <= len(self.matrix) - 1):
            return True
        else:
            return False


    def check_living():
        pass
