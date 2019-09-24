def guess_number_game():
	user_guess = int(input('Try to guess the number: '))
	guess_number = 7
	if user_guess < guess_number:
		print('Too low')
	elif user_guess > guess_number:
		print('Too high')
	elif user_guess == guess_number:
		print('Just right')
	else:
		print("You didn't put in a number")
guess_number_game()
guess_again = str(input('Want to guess again? '))
y = ['y','ya','yea','yeah','yes','yup']
while guess_again in y:
	guess_number_game()
	guess_again = str(input('Want to guess again? '))
	y = ['y','ya','yea','yeah','yes','yup']
else:
	print('thanks for playing')
