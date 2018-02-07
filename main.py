


from colorama import init
from colorama import Fore, Back, Style
from termcolor import colored


init()

def printBall(color):
	print(Back.WHITE + Style.BRIGHT + colored("O", color),end="")

class Board:
	def __init__(self,x_dim,y_dim):
		self.x = x_dim
		self.y = y_dim
		self.description = "Mastermind Game Board"
		self.author = "Evan Reilly"
		self.Board = []
		for j in range(x_dim):
			column = []
			for i in range(y_dim):
				column.append("O")
			self.Board.append(column)

	def printBoard(self):
		 for j in range(len(self.Board)):
		 	for i in range(len(self.Board[j])):
		 		print(Back.WHITE + " ",end="")
		 		printBall("grey") 
		 		print(Back.WHITE + " ",end="")
		 	print(""+Style.RESET_ALL)

		#print(self.Board[1])


gameBoard = Board(10,4)
gameBoard.printBoard()
# # then use Termcolor for all colored text output
# print(colored('Hello, World!', 'green', 'on_red'))
# print(colored('O', 'cyan'))
# print(colored('O', 'red')+colored('O','cyan'))


# print(Fore.RED + 'some red text')
# print(Back.GREEN + 'and with a green background')
# print(Style.BRIGHT + 'and in dim text')
# print(Style.RESET_ALL)
# print('back to normal now')



#prints colored ball
#def printBall(color):
#	print(Back.WHITE + Style.BRIGHT + colored("O", color),end="")




# for k in range (0,10):
# 	for i in range(0,4):
# 		#printBall(guessArray[i][k])
# 		print(Back.WHITE + "   ",end="")
# 	print("")
# 	print("")
print("Welcome to Mastermind!  Codemaker vs CodeBreaker!")


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
# 		feedback