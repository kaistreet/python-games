import random
from multiprocessing.pool import ThreadPool
def randomizer():
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
