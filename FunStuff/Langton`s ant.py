# Langton`s ant realization

from tkinter import *

class Ant():
	
	def __init__(self, x, y):
		self.nextPosition = [x - 1, y]
		self.currentX = x
		self.currentY = y
		self.cellColor = "Navy"

	def TurnLeft(self): # Turn Left if current cell is Grey
		
		if self.currentX - self.nextPosition[0] == 1:
			self.currentX, self.currentY = self.nextPosition
			self.nextPosition = [self.currentX, self.currentY - 1]
		
		elif self.currentX - self.nextPosition[0] == -1:
			self.currentX, self.currentY = self.nextPosition
			self.nextPosition = [self.currentX, self.currentY + 1]

		elif self.currentY - self.nextPosition[1] == 1:
			self.currentX, self.currentY = self.nextPosition
			self.nextPosition = [self.currentX + 1, self.currentY]
		
		elif self.currentY - self.nextPosition[1] == -1:
			self.currentX, self.currentY = self.nextPosition
			self.nextPosition = [self.currentX - 1, self.currentY]


	def TurnRight(self): # Turn Right if current cell is White

		if self.currentX - self.nextPosition[0] == 1:
			self.currentX, self.currentY = self.nextPosition
			self.nextPosition = [self.currentX, self.currentY + 1]
		
		elif self.currentX - self.nextPosition[0] == -1:
			self.currentX, self.currentY = self.nextPosition
			self.nextPosition = [self.currentX, self.currentY - 1]

		elif self.currentY - self.nextPosition[1] == 1:
			self.currentX, self.currentY = self.nextPosition
			self.nextPosition = [self.currentX - 1, self.currentY]
		
		elif self.currentY - self.nextPosition[1] == -1:
			self.currentX, self.currentY = self.nextPosition
			self.nextPosition = [self.currentX + 1, self.currentY]

	def Move(self):

		
		if (self.cellColor == "Navy"):
			
			try:
				print("Ant currently looks at {}, turning left now".format(self.nextPosition))

				self.TurnRight()

				canvas.itemconfig(gridRectangles[ant.currentX][ant.currentY], fill = 'MediumSeaGreen')
					
			
				nextCell = gridRectangles[self.nextPosition[0]][self.nextPosition[1]]

				self.cellColor = canvas.itemcget(nextCell, "fill")
				print("next cell color: {}".format(self.cellColor))

				print("Ant moves to {} {}".format(self.currentX, self.currentY))

				canvas.itemconfig(gridRectangles[self.nextPosition[0]][self.nextPosition[1]], fill = 'Fuchsia')

			except IndexError:
				print(self.currentX, self.currentY, " Yup you failed!")	
			
		else:

			try:

				print("Ant currently looks at {}, turning right now".format(self.nextPosition))

				self.TurnLeft()

				canvas.itemconfig(gridRectangles[ant.currentX][ant.currentY], fill = 'Navy')

				nextCell = gridRectangles[self.nextPosition[0]][self.nextPosition[1]]
				self.cellColor = canvas.itemcget(nextCell, "fill")
				print("next cell color: {}".format(self.cellColor))

				print("Ant moves to {} {}".format(self.currentX, self.currentY))

				canvas.itemconfig(gridRectangles[self.nextPosition[0]][self.nextPosition[1]], fill = 'Fuchsia')

			except IndexError:
				print(self.currentX, self.currentY, " Yup you failed!")

def SetupField(): # Sets up a matrix of rectangles to visualize algorithm

	global gridRectangles
	gridRectangles = []
	antMovementGrid = []
	x = 10
	y = 10

	for i in range(70):
		gridRectangles.append([])
		for k in range(70):
			rectangle = canvas.create_rectangle(x, y, x + 10, y + 10, fill = 'Navy')
			gridRectangles[i].append(rectangle)
			x += 10
		x = 10
		y += 10

def UnleashAnt(event): # Gets called once you click on field to spawn ant

	spawnX = int((event.y - event.y % 10) / 10 - 1)
	spawnY = int((event.x - event.x % 10) / 10 - 1)

	global ant
	ant = Ant(spawnX, spawnY)
	
	print("Ant unleashed on {} {}".format(ant.currentX, ant.currentY))

	canvas.itemconfig(gridRectangles[ant.currentX][ant.currentY], fill = 'Fuchsia') # Represents our ant


def Start():
	ant.Move()
	print("Ant currently looks at {}".format(ant.nextPosition))
	global begin_id
	begin_id = root.after(1, Start)

def Stop():
	root.after_cancel(begin_id)

root = Tk()


frame = Frame(root)
canvas = Canvas(frame, height = 720, width = 720)
SetupField()
frame.pack()
canvas.pack()


canvas.bind("<Button-1>", UnleashAnt)

startGame = Button(frame, text = "Start", command = Start)
startGame.pack(side = LEFT, padx = 5, pady = 5)

stopGame = Button(frame, text = "Stop", command = Stop)
stopGame.pack(side = RIGHT, padx = 5, pady = 5)

root.mainloop()