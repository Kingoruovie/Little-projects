#list are data structures we store multiple items. List are basically more like strings though they contain strings.now the same actions we take on strings can be takek on list.
#example
names = ['Samuel', 'Micheal', 'Sarah', 'Mosh', 'John']
print(names)
print(names[2])
print(names[2:-1])
print(names[-2].upper())
names[0] = 'Ovie'
print(names)

#we sometimes have what is called a 2D list. this is more like a matrix
#example
matrix = [
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9]
]
print(matrix)
print(matrix[0])
print(matrix[1][2])
#iteration
for row in matrix:
	for column in row:
		print(column)