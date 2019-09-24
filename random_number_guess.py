import random
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

randomizer()
play_again = str(input('want to play again? '))
y = ['y','ya','yee','yes','yup','ok','sure','mhmm','yeah','yea']
while play_again in y:
	randomizer()
	play_again = str(input('want to play again? '))
else:
	print('hope you enjoyed this game!')
