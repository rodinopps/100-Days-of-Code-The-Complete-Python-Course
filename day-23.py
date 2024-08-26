'''def rollDice():
  import random
  dice = random.randint(1, 6)
  print("You rolled", dice)'''

'''def rollDice():
  import random
  dice = random.randint(1, 6)
  print("You rolled", dice)

rollDice()
for i in range(100):
  rollDice()'''

'''def printMyName():
  print("My Name is David")

printMyName()'''

'''def countToFive():
  for i in range(1, 6):
    print(i)

countToFive()'''

'''def countToFive():
  for i in range(1, 6):
    print(i)

countToFive()'''

'''def printfavoritecolor():
  print("My favorite color is red.")

printfavoritecolor()'''

def system():
  while True:
    user = input("What is your username? ")
    password = input("What is your password? ")

    if user == "david" and password == "baldies4life":
      print("Welcome to Replit! ")
      exit()
    else:
      print("Whoops! I don't recognize that username or password. Try again!")

system()