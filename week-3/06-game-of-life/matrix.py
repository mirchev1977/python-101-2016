from cell import Cell


class Matrix:
    def __init__(self):
        self.living_cells = []
        self.coord_list = []

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

