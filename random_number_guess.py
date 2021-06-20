"""
This script asks a user to guess a number 1-9 and tells the user whether the number guessed is correct or incorrect. Additionally, the script loops if the user wants to play multiple times.

Author: Kai Street
Date: 22 September 2019

"""
import random
from multiprocessing.pool import ThreadPool

def randomizer():
	"""
	This function asks a user to guess a number 1-9, then tells the user whether the number guessed is correct or incorrect.

	Author: Kai Street
	Date: 22 September 2019

	Precondition: ask_user_number must be int type
	"""
	rando_numbered_list = random.randint(1,9)
	ask_user_number = int(input('Guess a number between 1 and 9: '))
	if ask_user_number == rando_numbered_list:
		print('you guessed correctly! the number was:',rando_numbered_list)
	elif ask_user_number > rando_numbered_list:
		print('you guessed too high! the number was:',rando_numbered_list)
	elif ask_user_number < rando_numbered_list:
		print('you guessed too low! the number was:',rando_numbered_list)
	else:
		print("i don't think you guessed a number")

#Ask if user wants to run randomizer function, then loop if user wants to play multiple times; leverages multiprocessing to speed up output.
pool = ThreadPool(processes=4)
pool.apply(randomizer)
pool.close()
play_again = str(input('want to play again? [enter y if yes] '))
while play_again[1] == 'y':
	pool = ThreadPool(processes=4)
	pool.apply(randomizer)
	pool.close()
else:
	print('hope you enjoyed this game!')
