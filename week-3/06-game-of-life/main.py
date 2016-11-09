from matrix import Matrix
import os
import time


def main():
    matrix = Matrix()
    matrix.input_living_cells()
    dimensions = matrix.find_matrix_dimensions()
    matrix.fill_matrix_with_dead(dimensions)
    matrix.fill_matrix_with_living()
    os.system('clear')

    for i in range(30):
        matrix.print_matrix()
        matrix.iterate_over_matrix()
        matrix.change_cell_states()
        time.sleep(2)
        os.system('clear')


if __name__ == "__main__":
    main()
