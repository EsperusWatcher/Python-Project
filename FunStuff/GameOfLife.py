from tkinter import *

class Cell():

	def __init__(self, x, y, i, j):
		self.isAlive = False
		self.nextCondition = None # Determines whether cell ig going to die next it or no
		self.gridPosition = (x, y)
		self.matrixPosition = (i, j)

	def __str__(self):
		return str(self.isAlive)

	def __repr__(self):
		return str(self.isAlive)

	def changeState(self):
		self.isAlive = not self.isAlive

def getClickedRectangle(x, y):
	return (x - x%10, y - y%10)


def setupGameField():
	# Setting up the game field with 70x70 grid
	global gridRectangles
	global gridCells 
	gridRectangles = [] 
	gridCells = [] 
	y = 10
	x = 10
	for i in range(70):
		gridRectangles.append([])
		gridCells.append([])
		for k in range(70):
			rectangle = canvas.create_rectangle(x, y, x+10, y+10, fill = 'Snow')
			gridRectangles[i].append(rectangle)
			gridCells[i].append(Cell(x, y, i, k))
			x += 10
		x = 10
		y += 10

def changeColorOnClick(event):
	print(event.x, event.y)
	x, y = getClickedRectangle(event.x, event.y)
	try:
		ix = int(y/10 - 1) 
		iy = int(x/10 - 1)
		if ix == -1 or iy == -1:
			raise IndexError
		if gridCells[ix][iy].isAlive:
			canvas.itemconfig(gridRectangles[ix][iy], fill = 'Snow')
		else:
			canvas.itemconfig(gridRectangles[ix][iy], fill = 'Black')
		gridCells[ix][iy].changeState()
		print(gridCells[ix][iy].gridPosition, gridCells[ix][iy].matrixPosition)
	except IndexError:
		return


def paintGrid():
	for i in gridCells:
		for j in i:
			if j.nextCondition != j.isAlive:
				x, y = j.matrixPosition
				print (x, y)
				if j.nextCondition:
					canvas.itemconfig(gridRectangles[x][y], fill = 'Black')
					print ("changed", j.matrixPosition, "from dead to alive")
				else:
					canvas.itemconfig(gridRectangles[x][y], fill = 'Snow')
					print ("changed", j.matrixPosition, "from alive to dead")
				j.changeState()
				print ("Current status of", j.matrixPosition, j.isAlive)
					


def ChangeInStatus(cell):
	# Checks cells around and returns True or False based on the next status of current cell
	num_alive = 0
	x, y = cell.matrixPosition
	for i in (x - 1, x, x + 1):
		for j in (y - 1, y, y + 1):
			if i == x and j == y:
				continue
			if i == -1 or j == -1:
				continue
			try:
				if gridCells[i][j].isAlive:
					num_alive += 1
			except IndexError:
				pass
	if cell.isAlive:
		return not( num_alive == 2 or num_alive == 3 )
	else:
		return num_alive == 3

def StartGame():
	for i in gridCells:
		for j in i:
			if ChangeInStatus(j):
				j.nextCondition = not j.isAlive
				print ("change in", j.matrixPosition, "from", j.isAlive, "to", j.nextCondition)
			else:
				j.nextCondition = j.isAlive
	paintGrid()
	global begin_id
	begin_id = root.after(80, StartGame)


def StopGame():
	root.after_cancel(begin_id)


root = Tk()
frame = Frame(root)

root.title("Game of life")

canvas = Canvas(frame, width = 720, height = 720)
canvas.place(anchor = CENTER)

setupGameField()

line1 = canvas.create_line(0,0,0,720, width = 10)
line2 = canvas.create_line(0,720,720,720, width = 5)
line3 = canvas.create_line(720,720,720,0, width = 5)
line4 = canvas.create_line(720,0,0,0,  width = 10)

canvas.pack()
frame.pack()

canvas.bind("<Button-1>", changeColorOnClick)

startGame = Button(frame, text = "Start", command = StartGame)
startGame.pack(side = LEFT, padx = 5, pady = 5)
stopGame = Button(frame, text = "Stop", command = StopGame)
stopGame.pack(side = RIGHT, padx = 5, pady = 5)
root.mainloop()

