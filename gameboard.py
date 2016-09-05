"""Gameboard Generator"""

columns = int(raw_input("How many columns do you want on your gameboard? "))
rows = int(raw_input("How many rows do you want on your gameboard? "))
def gameboard(columns,rows):
	column = []
	height = []
	for i in range(columns):
		column.append("|    |")
	for i in range(columns):
		height.append(" ---- ")
	for i in range(rows):
		print "".join(height)
		print "".join(column)
		print "".join(height)
	return column,height
gameboard(columns,rows)