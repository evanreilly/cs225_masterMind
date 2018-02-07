


from colorama import init
from colorama import Fore, Back, Style
from termcolor import colored


# use Colorama to make Termcolor work on Windows too
init()

# # then use Termcolor for all colored text output
# print(colored('Hello, World!', 'green', 'on_red'))
# print(colored('O', 'cyan'))
# print(colored('O', 'red')+colored('O','cyan'))


# print(Fore.RED + 'some red text')
# print(Back.GREEN + 'and with a green background')
# print(Style.BRIGHT + 'and in dim text')
# print(Style.RESET_ALL)
# print('back to normal now')


def printBall(color):
	print(Style.BRIGHT + colored("O", color),end="")
	
printBall("red")
print("")
printBall("cyan")
printBall("green")
printBall("white")
print(Style.DIM+colored('Some bright red text',"red"))
#printBall()
print(Fore.RED+Style.BRIGHT+'Some bright red text')

person = input('Enter your name: ')
print('Hello', person)


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