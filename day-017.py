'''while True:
  print("You are in a corridor, do you go left or right?")
  direction = input("> ")
  if direction == "left":
    print("You have fallen to your death")
    break'''

'''while True:
  print("You are in a corridor, do you go left or right?")
  direction = input("> ")
  if direction == "left":
    print("You have fallen to your death")
    break
  elif direction == "right":
    continue
  else:
    print("Ahh! You're a genius, you've won")'''

'''while True:
  print("You are in a corridor, do you go left or right?")
  direction = input("> ")
  if direction == "left":
    print("You have fallen to your death")
    break
  elif direction == "right":
    continue
  else:
    print("Ahh! You're a genius, you've won")
    exit()
print("The game is over, you've failed!")'''

'''while True:
  print("You are in a corridor, do you go left or right?")
  direction = input("> ")
  if direction == "left":
    print("You have fallen to your death")
    break
  elif direction == "right":
    continue
  else:
    print("Ahh! You're a genius, you've won")
    exit()
print("The game is over, you've failed!")'''

'''print("Let's play chutes and ladders. Pick ladder or chute.")
while True:
  print("Do you want to go up the ladder or down the chute?")
  direction = input("> ")
  if direction == "chute":
    print("Game over!")
    break
  elif direction == "ladder":
    continue
  else:
    print("Game over!")
    exit()
print("Thanks for playing!")'''

from getpass import getpass as input
score1 = 0
score2 = 0
while True:
  p1 = input("R, P or S? ")
  p2 = input("R, P or S? ")

  if p1 == "S" and p2 == "P":
    print("Player 1 has won this round. ")
    score1 += 1
  elif p1 == "S" and p2 == "R":
    print("Player 2 has won this round. ")
    score2 += 1
  elif p1 == "S" and p2 == "S":
    print("Draw. Try again. ")

  elif p1 == "R" and p2 == "S":
    print("Player 1 has won this round. ")
    score1 += 1
  elif p1 == "R" and p2 == "R":
    print("Draw. Try again. ")
  elif p1 == "R" and p2 == "P":
    print("Player 2 has won this round. ")
    score2 += 1

  elif p1 == "P" and p2 == "P":
    print("Draw. Try again. ")
  elif p1 == "P" and p2 == "R":
    print("Player 1 has won this round. ")
    score1 += 1
  elif p1 == "P" and p2 == "S":
    print("Player 2 has won this round. ")
    score2 += 1

  if score1 == 3:
    print("Player 1 has won. ")
    break
  elif score2 == 3:
    print("Player 2 has won. ")
    break
  else:
    continue
