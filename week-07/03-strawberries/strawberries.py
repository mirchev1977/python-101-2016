class Strawberry:
	"""docstring for Strawberry"""
	def __init__(self):
		self.row = None
		self.col = None
		self.isAlive = True



def strawberries(rows, columns, days, dead_strawberries):
	matrix = []
	for row in range(rows):
		row_line = []
		for col in range(columns):
			strawberry = Strawberry()
			strawberry.raw = row
			strawberry.col = col
			strawberry.isAlive = True

			for dead_straberry in dead_strawberries:
				dead_raw = dead_straberry[0]
				dead_col = dead_straberry[1]
				if row == dead_raw and col == dead_col:
					strawberry.isAlive = False



			row_line.append(strawberry)

		matrix.append(row_line)

	for day in range(days):
		for row  in range(rows):
			for col in range(columns):
				current = matrix[row][col]
				if current.isAlive == False:
					if row - 1 >= 0:
						matrix[row - 1][col].isAlive = False
					if col - 1 >= 0:
						matrix[row][col - 1].isAlive = False
					if col + 1 < columns:
						matrix[row][col + 1].isAlive = False
					if row + 1 < rows:
						matrix[row + 1][col].isAlive = False

	counter = 0
	for row in matrix:
		for strawberry in row:
			if strawberry.isAlive == True:
				counter += 1
			# print(strawberry.raw, strawberry.col, strawberry.isAlive)

	return counter


# strawberries(8, 10, 2, [(4, 8), (2, 7)])
# strawberries(8000, 10, 2, [(4, 8), (2, 7)])
# strawberries(8, 10, 11, [(4, 8), (2, 7)])