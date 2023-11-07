# Mayo 7, 2023. 01:02
# Este código simplemente me solucionará la vida

def tprint(title, content, columns):

	# Convert the table to str

	for index, cell in enumerate(content):
		content[index] = str(cell)

	# Get the width of each column and of the whole table in characters

	max_widths = [0] * columns
	table_width = 0
	row_width = (columns - 1) * 4

	for index, cell in enumerate(content):
		if len(cell) > max_widths[index % columns]:
			max_widths[index % columns] = len(cell)
		if len(content) - index <= columns: # 1, 2, 3    4, 5, 6
			row_width += max_widths[index % columns]

	if row_width < len(title):
		table_width = len(title)

	# Create the string to be printed

	if table_width:
		string = title + "\n" + ("=" * table_width) + "\n"
	else:
		string = " " * int((row_width - len(title)) / 2) + title + " " * int((row_width - len(title)) / 2) + "\n" + "=" * row_width + "\n"

	for index, cell in enumerate(content):

		# Add a line break instead of four spaces if we arrived to the final column

		if index % columns == columns - 1:
			string += cell + "\n"
			continue

		# Add the cell with certain extra spacing if the title is larger than the rows

		if table_width:
			string += cell + " " * (max_widths[index % columns] - len(cell) + 4 + int((table_width - row_width) / (columns - 1)))
			continue

		# Add the cell and the corresponding spacing after it

		string += cell + " " * (max_widths[index % columns] - len(cell) + 4)

	# Print the table

	return string

# Mayo 7, 2023. 01:26
# Mayo 7, 2023. 01:28. Agregaré que se imprima el nombre de la tabla
# Mayo 7, 2023. 01:53
# Mayo 7, 2023. 02:35. Agregaré que si el título es más largo, la longitud de la tabla sea la del título
# Mayo 7, 2023. 03:14. Luego de experimentar con centrar y alinear a la derecha celdas, así quedó el código
# Mayo 7, 2023. 09:03. Editando para que esto acepte todo tipo de datos
# Mayo 7, 2023. 09:04. Terminado