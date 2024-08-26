'''import random
myNumber = random.randint(1,100)
print(myNumber)'''

'''import random

myNumber = random.randint(1, 100)
print(myNumber)'''

'''import random

for i in range(10):
  myNumber = random.randint(1, 100)
  print(myNumber)'''

'''import random

for i in range(10):
  myNumber = random.randint(1, 10)
  print(myNumber)'''

import random
number = random.randint(1, 1000000)
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