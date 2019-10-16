#Make a two-player Rock-Paper-Scissors game.
import sys
print("Let's play ro sham bo!")
player_1 = str(input('Player 1, enter your name: '))
print('Hi ' + player_1 + '!')
player_2 = str(input('Player 2, enter your name: '))
print('Hi ' + player_2 + '!')
y = ['y','yes','yup','yeah','yea','ya']
ready_p1 = str(input(player_1 + ', are you ready? '))
if ready_p1 in y:
  print('ok!')
  ready_p2 = str(input(player_2 + ', are you ready? '))
  if ready_p2 in y:
    print('ok!')
else:
  print("alright, we won't play then.")
  sys.exit()
def roshambo():
  rock = ['rock','r']
  paper = ['paper','p']
  scissors = ['scissors','s']
  rps_1 = str(input(player_1 + '! Rock, Paper or Scissors? '))
  rps_2 = str(input(player_2 + '! Rock, Paper or Scissors? '))
  if ((rps_1 in rock) and (rps_2 in scissors)):
    print(player_1 + ' wins! sorry ' + player_2)
  elif ((rps_1 in paper) and (rps_2 in rock)):
    print(player_1 + ' wins! sorry ' + player_2)
  elif ((rps_1 in scissors) and (rps_2 in paper)):
    print(player_1 + ' wins! sorry ' + player_2)
  elif ((rps_2 in rock) and (rps_1 in scissors)):
    print(player_2 + ' wins! sorry ' + player_1)
  elif ((rps_2 in paper) and (rps_1 in rock)):
    print(player_2 + ' wins! sorry ' + player_1)
  elif ((rps_2 in scissors) and (rps_1 in paper)):
    print(player_2 + ' wins! sorry ' + player_1)
  elif rps_1 == rps_2:
    print("it's a tie!")
roshambo()
play_again = str(input('want to play again? '))
y = ['y','yes','yup','yeah','yea','ya']
while play_again in y:
  roshambo()
  play_again = str(input('want to play again? '))
else:
  print('hope you had fun!')
  sys.exit()
