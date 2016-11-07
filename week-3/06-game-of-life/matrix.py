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

