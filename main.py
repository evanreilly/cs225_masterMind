from colorama import init
from colorama import Fore, Back, Style
from termcolor import colored
import random
import re

#important for colorama to work with windows, look at 
#colorama documentation for more information 
init()

# printBall method prints the ball with specified color as the letter O
def printBall(color):
	print(Back.WHITE + Style.BRIGHT + colored("O", color),end="")

# Game class
class Game: 
	#Constructor
	def __init__(self,x_dim,y_dim):
		self.x = x_dim #x dimension
		self.y = y_dim #y dimension
		self.description = "Mastermind Game Board"
		self.author = "Evan Reilly, Sarah Pell, Alec Ray"
		self.Board = [] #init board
		self.Code = [] #init the mastermind code

		# build the board
		for j in range(x_dim):
			column = []
			for i in range(y_dim):
				column.append("O")
			self.Board.append(column)

	#setRow method sets the row
	def setRow(self, row, replacementRow):
		self.Board[row][:] = [] #delete row as it is
		self.Board[row] = replacementRow

	#setCode method sets the current code
	def setCode(self, code):  
		for i in code:
			self.Code.append(i)

	#checkCode method checks the current code
	def checkCode(self, row):
		for i in range(len(self.Code)):
			if row[i] != self.Code[i]:
				return False
		return True

	#codeFeedback method returns the feedback of which colored balls are in the right positions
	def codeFeedback(self, row):
		feedback = []
		for i in range(len(row)):
			if self.Code[i] == row[i]:
				feedback.append("red")
			elif row[i] in self.Code:
				feedback.append("white")
		return feedback

	#setRandomCode method chooses a random code for the player to guess
	def setRandomCode(self):
		colorArray = ['red','green','yellow','cyan','magenta','white']
		randomCode = []
		for i in range(0,4):
			temp = random.randint(0,5)
			randomCode.append(colorArray[temp])
		self.Code = randomCode

	#printBoard method prints out the actual game board
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
	if re.match('(?=[rgycmw]{4,4}$).*',guess):
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
		if guess[i] == "c":
			parsed.append("cyan")
		if guess[i] == "m":
			parsed.append("magenta")
		if guess[i] == "w":
			parsed.append("white")

	#inverse parse
	for i in range(len(guess)):
		if guess[i] == "red":
			parsed.append("r")
		if guess[i] == "green":
			parsed.append("g")
		if guess[i] == "yellow":
			parsed.append("y")
		if guess[i] == "cyan":
			parsed.append("c")
		if guess[i] == "magenta":
			parsed.append("m")
		if guess[i] == "white":
			parsed.append("w")
	return parsed 

#as of now, just random guess generated for computer
def pc_guess():
	colorArray = ['red','green','yellow','cyan','magenta','white']
	randomCode = []
	for i in range(0,4):
		temp = random.randint(0,5)
		randomCode.append(colorArray[temp])

	return randomCode


#user creates code, computer guesses
def codeMaker():
	print("""
		Create your code for the computer to break!

		Color options:
		red
		green
		yellow
		cyan
		magenta
		white
						
		""")

	code = input("Enter your code: ")
	print("code size: ",len(code))
	gameBoard = Game(10,4)
	gameBoard.setCode(code)
	#gameBoard.printBoard()
	
	guesses = 0
	maxGuesses = 10

	while (guesses < maxGuesses ):
		pcGuess = pc_guess()
		
		parsedGuess = parseGuess(pcGuess)
		
		gameBoard.setRow(guesses,parsedGuess)
		
		win = gameBoard.checkCode(parsedGuess)
		#gameBoard.printBoard()
		guesses+=1

		#print(win)
		if(win==True):
		#gameBoard.printBoard()
				print("Computer Wins!, "+ str(guesses) +" guess(es)")
		
	if(win==False):
		print("Computer loses after " + str(guesses) + " guess(es)")
	#rigged(code,gameBoard)
	
def rigged(code,gameBoard):
	parsedGuess = parseGuess(code)
	print("parsedGuess: ",parsedGuess)
	gameBoard.setRow(9,parsedGuess)
	gameBoard.printBoard()
	print("""
		The system was and always has been rigged.
		Computers will always win.
		Your code was
		""" + str(gameBoard.Code))



#user plays against computer generated code
def codeBreaker():
	gameBoard = Game(10,4)
	#gameBoard.setCode("yellow","green","yellow","green")
	gameBoard.setRandomCode()
	gameBoard.printBoard()
	print("""
		Crack the computer's code...

		Color options:
		red
		green
		yellow
		cyan
		magenta
		white
						
		""")
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
			gameBoard.printBoard()
			# print("valid guess")
		else:
			print("invalid input")

	print("You Lose! " +str(maxGuesses)+" exceeded!")
	print("The code was "+str(gameBoard.Code))
	

def main(): 
	end = False
	while (end == False):
		print("""
			Welcome to Mastermind!
			What would you like to do?
			1. Be the codemaker
			2. Be the codebreaker
			3. Help!
			4. Quit
			""")
		answer = input("Enter a number: ")

		if answer == "1":
			codeMaker()

		elif answer == "2":
			codeBreaker()

		elif answer == "3":
			print("""
		Instructions:

		Codemaker mode:
		Enter the first letters of the color options.
		You can choose four colors for the code.
		The computer will then proceed to try and crack it in 10 tries.
		Sit back and relax.

		Codebreaker mode:
		The computer will create a combination of 4 colors.
		Your goal is to try and figure out that combination in 10 guesses.
		You can guess four colors at a time. Order matters.
		For each guess, you get some hints!
			Red means that your peg has the right color and position.
			White means that your peg has the right color but wrong position.

		Good luck!
				""")

		elif answer == "4":
			print("Hope it worked! Byeeee")
			end = True

		else:
			print("That wasn't an option...")
			
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