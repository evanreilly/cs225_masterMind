

from colorama import init
from colorama import Fore, Back, Style
from termcolor import colored
import random
import re

#important for colorama to work with windows, look at 
#colorama documentation for more information 
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

	def setRow(self, row, replacementRow):
		self.Board[row][:] = [] #delete row as it is
		self.Board[row] = replacementRow

	def setCode(self, color1,color2,color3,color4):  
	 	self.Code = [color1, color2, color3, color4]

	def checkCode(self, row):
		for i in range(len(self.Code)):
			if row[i] != self.Code[i]:
				return False
		return True

	def codeFeedback(self, row):
		feedback = []
		for i in range(len(row)):
			if self.Code[i] == row[i]:
				feedback.append("red")
			elif row[i] in self.Code:
				feedback.append("white")
		return feedback

	def setRandomCode(self):
		colorArray = ['red','green','yellow','cyan','magenta','white']
		randomCode = []
		for i in range(0,4):
			temp = random.randint(0,5)
			randomCode.append(colorArray[temp])
		self.Code = randomCode

	def printBoard(self):
		 for j in range(len(self.Board)):
		 	for i in range(len(self.Board[j])):
		 		print(Back.WHITE + " ",end="")
		 		if self.Board[j][i] == "O":
		 			printBall("grey") 
		 		else:
		 			printBall(self.Board[j][i])
		 		print(Back.WHITE + " ",end="")
		 	
		 	#if self.Board[j] != ["O", "O", "O", "O"]:
		 	feedBack = self.codeFeedback(self.Board[j])
		 	for k in range(len(feedBack)):
		 	 	printBall(feedBack[k])
		 	
		 	print(""+Style.RESET_ALL) #Fixes formatting

	# r g y b p w
	# red, green, yellow, blue (cyan), pink (magenta), white
def validateGuess(guess):
	if re.match('(?=[rgybpw]{4,4}$).*',guess):
		return True
	return False

def parseGuess(guess):
	parsed = []
	for i in range(len(guess)):
		if guess[i] == "r":
			parsed.append("red")
		if guess[i] == "g":
			parsed.append("green")
		if guess[i] == "y":
			parsed.append("yellow")
		if guess[i] == "b":
			parsed.append("cyan")
		if guess[i] == "p":
			parsed.append("magenta")
		if guess[i] == "w":
			parsed.append("white")
	return parsed 

def main(): 
	gameBoard = Game(10,4)
	#gameBoard.setCode("yellow","green","yellow","green")
	gameBoard.setRandomCode()
	gameBoard.printBoard()
	print("Welcome to Mastermind!  Codemaker vs CodeBreaker!")
	guesses = 0
	maxGuesses = 10
	while (guesses < maxGuesses):
		guess = input("Enter a guess:  ")
		if validateGuess(guess):
			parsedGuess = parseGuess(guess)
			gameBoard.setRow(guesses,parsedGuess)
			guesses+=1
			win = gameBoard.checkCode(parsedGuess)
			if win:
				gameBoard.printBoard()
				print("You Win!, "+ str(guesses) +" guesses")
			
			# print("valid guess")
		else:
			print("invalid input")

	print("You Lose! " +str(maxGuesses)+" exceeded!")
	print("The code was "+str(gameBoard.Code))
main()

######Psudo Code############
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


