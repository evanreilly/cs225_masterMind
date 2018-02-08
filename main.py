


from colorama import init
from colorama import Fore, Back, Style
from termcolor import colored
import random
import re


init()

def printBall(color):
	print(Back.WHITE + Style.BRIGHT + colored("O", color),end="")

class Game: 
	def __init__(self,x_dim,y_dim):
		self.x = x_dim
		self.y = y_dim
		self.description = "Mastermind Game Board"
		self.author = "Evan Reilly"
		self.Board = []
		self.Code = []
		for j in range(x_dim):
			column = []
			for i in range(y_dim):
				column.append("O")
			self.Board.append(column)

	def printBoard(self):
		 for j in range(len(self.Board)):
		 	for i in range(len(self.Board[j])):
		 		print(Back.WHITE + " ",end="")
		 		if self.Board[j][i] == "O":
		 			printBall("grey") 
		 		else:
		 			printBall(self.Board[j][i])
		 		print(Back.WHITE + " ",end="")
		 	print(""+Style.RESET_ALL) #Fixes formatting

	def setRow(self, row, color1, color2, color3, color4):
		self.Board[row][:] = [] #delete row as it is
		self.Board[row].append(color1)
		self.Board[row].append(color2)
		self.Board[row].append(color3)
		self.Board[row].append(color4)

	def setCode(self, color1,color2,color3,color4):  
		self.Code = [color1, color2, color3, color4]
	


	def checkCode(self, row):
		for i in range(len(self.Code)):
			if row[i] != Code[i]:
				return False
		return True

	def codeFeedback(self, row):
		feedback = []
		for i in range(len(row)):
			if self.Code[i] == row[i]:
				feedback.append("red")
			elif row[i] in self.Code:
				feedback.append("blue")
		return feedback







#
	

	# r g y b p w
	# red, green, yellow, blue (cyan), pink (magenta), white
def validateGuess(guess):
	if re.match('(rgybpw)*(?=.{4,4}$).*',guess):
		return True
	return False


def parseGuess(guess):
	print("parse")



def main(): 
	gameBoard = Game(10,4)
	#gameBoard.setRow(1,"red","cyan","green","yellow")

	gameBoard.printBoard()
	gameBoard.setCode("yellow","green","yellow","green")
	print("Welcome to Mastermind!  Codemaker vs CodeBreaker!")
	guesses = 0
	maxGuesses = 10
	while (guesses < maxGuesses):
		guess = input("Enter a guess:  ")
		if validateGuess(guess):
			print("valid guess")
		else:
			print("invalid input")


	print("")

main()




# print(Fore.RED + 'some red text')
# print(Back.GREEN + 'and with a green background')
# print(Style.BRIGHT + 'and in dim text')
# print(Style.RESET_ALL)
# print('back to normal snow')





gametype = input("")

printBall("red")
print("")
printBall("cyan")
printBall("green")
printBall("white")
print(Style.DIM+colored('Some bright red text',"red"))
#printBall()
print(Fore.RED+Style.BRIGHT+'Some bright red text')



# response
# red = 1 right color in right place
# white = 1 right color in wrong place

# Start screen

# welcome to mastermind!
# select your gametype
# 	user guesses 

#		generate a code from the computer of 4 colors in 4 spots
#		user gets 10 tries to guess colors/orders
#		input guesses with letter in specific position
#		feedback: response (see above)

# 	computer guesses
#		user comes up with a code for the computer to guess
#		computer gets 10 tries to guess the code

# 		feedback: response (see above)


# methods we need

# generate a random code of 4 colors/spots
# menu options
# read and interpret the code

# 		feedback


# Computer generates the code for the user to guess generate the code
def generateCode():
	# r g y b p w
	# red, green, yellow, blue (cyan), pink (magenta), white
	colorArray = ['r','g','y','b','p','w'] # all usable colors, red green yellow blue purple white
	
	positionArray = [] # position array

	for i in range(0,4):
		temp = random.randint(0,5)
		positionArray.append(colorArray[temp])

	print(positionArray)

generateCode()

