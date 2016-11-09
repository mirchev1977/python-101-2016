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

    for x in range(20):
        matrix.print_matrix()
        matrix.iterate_over_matrix()
        time.sleep(2)
        os.system('clear')


if __name__ == "__main__":
    main()
