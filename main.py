


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

print("Welcome to Mastermind!  Codemaker vs CodeBreaker!")



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