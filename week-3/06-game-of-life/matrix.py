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

        print()


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
                living_dead_neighbors = self.check_neighbors(current)
                living_neighbors = living_dead_neighbors[0]
                dead_neighbors = living_dead_neighbors[1]
                self.change_state_of_cell(
                    current, living_neighbors, dead_neighbors)

    def change_state_of_cell(self, cell, living, dead):
        if cell.isAlive:
            if living < 2 and dead >= 3:
                cell.isAlive = False
            return

        if cell.isAlive is False:
            if living >= 3:
                cell.isAlive = True
            return

    def check_neighbors(self, cell):
        neighbors = ((-1, -1), (-1, 0), (-1, 1),
                     (0, -1), (0, 1),
                     (1, -1), (1, 0), (1, 1))
        count_valid = 0
        count_living = 0
        count_dead = 0
        for neighbor in neighbors:
            neighbor_cell = is_valid = self.neighbor_is_valid(neighbor, cell)
            if is_valid:
                neighbor_cell = self.get_neighbor_cell(neighbor, cell)
                if neighbor_cell.isAlive:
                    count_living += 1
                else:
                    count_dead += 1
                count_valid += 1
        return (count_living, count_dead)

    def get_neighbor_cell(self, neighbor, cell):
        row = cell.row + int(neighbor[0])
        col = cell.col + int(neighbor[1])
        neighbor_cell = self.matrix[row][col]
        return neighbor_cell

    def neighbor_is_valid(self, neighbor, cell):
        neigh_row = neighbor[0]
        neigh_col = neighbor[1]
        one = cell.row + int(neigh_row) >= 0
        two = cell.row + int(neigh_row) <= len(self.matrix) - 1
        three = cell.col + int(neigh_col) >= 0
        four = cell.col + int(neigh_col) <= len(self.matrix) - 1
        if one and two and three and four:
            return True
        else:
            return False
