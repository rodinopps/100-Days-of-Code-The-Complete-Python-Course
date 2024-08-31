'''myString = "Day 38"
for letter in myString:
  print(letter)

# This code outputs:
#D
#a
#y

#3
#8
# this is a comment in the code, the computer will ignore it'''

'''myString = "Day 38"
for letter in myString:
  if letter.lower() == "a":
    print('\033[33m', end='') #yellow
  print(letter)
  print('\033[0m', end='') #back to default

# This code outputs (with a yellow 'a'):
#D
#a
#y

#3
#8'''

'''vowels = ["a","e","i","o","u"]

myString = "Will my vowels now be yellow?"
for letter in myString:

  if letter.lower() in vowels:
    print('\033[33m', end='') #yellow

  print(letter, end="")
  print('\033[0m', end='') #back to default'''

words = input("Enter a string: ")
for i in words:
  if i == "r":
    print("\033[31m", end="")
  elif i == " ":
    print("\033[0m", end="")
  elif i == "b":
    print("\033[34m", end="")
  elif i == "y":
    print("\033[33m", end="")
  elif i == "g":
    print("\033[32m", end="")
  elif i == "p":
    print("\033[35m", end="")
  print(i, end = "")

  
    
    