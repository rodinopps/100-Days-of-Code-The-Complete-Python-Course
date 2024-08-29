number = 567896
turn = 0
while True:
  guess = int(input("Guess a number: "))
  if guess > number:
    print("Lower. ")
    turn += 1
  elif guess < number:
    print("Higher. ")
    turn += 1
  elif guess < 0:
    exit()
  else:
    print("You have guessed correctly with", turn, "tries. ")
    break
