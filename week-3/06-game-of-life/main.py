from matrix import Matrix


def main():
    matrix = Matrix()
    matrix.input_living_cells()
    dimensions = matrix.find_matrix_dimensions()
    matrix.fill_matrix_with_dead(dimensions)
    matrix.fill_matrix_with_living()
    matrix.iterate_over_matrix()


if __name__ == "__main__":
    main()
