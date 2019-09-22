"""Problem 8:
Make a two-player Rock-Paper-Scissors game.
"""
print("Let's play ro sham bo!")
user_one_name = str(input('Ready player one? Tell me your name: '))
print('Welcome',user_one_name)
user_two_name = str(input('Ready player two? Tell me your name: '))
print('Welcome',user_two_name)

def roshambo():
	rock = ['r','ro','roc','rock','stone','boulder','pebble']
	paper = ['p','pa','pap','pape','paper','sheet']
	scissors = ['s','sc','sci','scis','sciss','scisso','scissor','scissors','shears','cut']
	user_one_rps = str(input('Hey player one! Rock, paper or scissors?'))
	user_two_rps = str(input('Hey player two! Rock, paper or scissors?'))
	if ((user_one_rps in rock) and (user_two_rps in scissors)):
		print('player one wins! sorry player two!')
	elif ((user_one_rps in paper) and (user_two_rps in rock)):
		print('player one wins! sorry player two!')
	elif ((user_one_rps in scissors) and (user_two_rps in paper)):
		print('player one wins! sorry player two!')
	elif ((user_two_rps in rock) and (user_one_rps in scissors)):
		print('player two wins! sorry player one!')
	elif ((user_two_rps in paper) and (user_one_rps in rock)):
		print('player two wins! sorry player one!')
	elif ((user_two_rps in scissors) and (user_one_rps in paper)):
		print('player two wins! sorry player one!')
	else:
		print("you're not playing the game right!")

roshambo()
play_again = str(input('want to play again?'))
y = ['y','ya','yes','yup','yea','yeah','yup','mhmm','sure']
while play_again in y:
	roshambo()
	play_again = str(input('want to play again? '))
else:
	print('hope you had fun!')
