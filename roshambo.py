"""
This script plays the iconic game, Roshambo.

Author: Kai Street
Date: 22 September 2019
"""
import random,time

def roshambo():
	"""
	This function allows two players to play the iconic game, Roshambo.

	Author: Kai Street
	Date: 22 September 2019

	Precondition: user_one_name and user_two_name must both be string types
	"""
	
	#Starts game
	print("Let's play ro sham bo!")
	time.sleep(random.uniform(0.1,0.3))

	#Welcomes users to game
	user_one_name = input('Ready player one? Tell me your name: ')
	assert type(user_one_name) == str,'User name is not a string'
	print('Welcome',user_one_name)
	time.sleep(random.uniform(0.1,0.3))

	user_two_name = input('Ready player two? Tell me your name: ')
	assert type(user_two_name) == str,'User name is not a string'
	print('Welcome',user_two_name)
	time.sleep(random.uniform(0.1,0.3))

	#Asks users for their move
	user_one_rps = str(input('Hey player one! rock, paper or scissors? '))
	user_two_rps = str(input('Hey player two! rock, paper or scissors? '))

	#Checks answers against each other
	if ((user_one_rps == 'rock') and (user_two_rps == 'scissors')):
		print('player one wins! sorry player two!')
	elif ((user_one_rps == 'paper') and (user_two_rps == 'rock')):
		print('player one wins! sorry player two!')
	elif ((user_one_rps == 'scissors') and (user_two_rps == 'paper')):
		print('player one wins! sorry player two!')
	elif ((user_two_rps == 'rock') and (user_one_rps == 'scissors')):
		print('player two wins! sorry player one!')
	elif ((user_two_rps == 'paper') and (user_one_rps == 'rock')):
		print('player two wins! sorry player one!')
	elif ((user_two_rps == 'scissors') and (user_one_rps == 'paper')):
		print('player two wins! sorry player one!')
	elif user_one_rps == user_two_rps:
		print('it"s a tie!')
	else:
		print("you're not playing the game right!")

#Starts game; allows users to loop if they want to play multiple rounds.
roshambo()
play_again = str(input('want to play again? [enter "y" if yes]: '))
while play_again == 'y':
	roshambo()
	play_again = str(input('want to play again? '))
else:
	print('hope you had fun!')
