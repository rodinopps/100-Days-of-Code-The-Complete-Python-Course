'''while True:
  print("This program is running")
print("Aww, I was having a good time 😭")'''

'''while True:
  print("This program is running")
  goAgain = input("Go again?: ")
  if goAgain == "no":
    break
print("Aww, I was having a good time 😭")'''

'''counter = 0
while True:
  answer = int(input("Enter a number: "))
  print("Adding it up!")
  counter += answer
  print("Current total is", counter)
  addAnother = input("Add another? ")
  if addAnother == "no":
    break
print("Bye!")'''

'''counter = 0
while True:
  answer = int(input("Enter a number: "))
  print("Adding it up!")
  counter += answer
  print("Current total is", counter)
  addAnother = input("Add another? ")
  if addAnother == "no":
    print("Bye!")
    break'''

'''while True:
  color = input("Enter a color: ")
  if color == "red":
    break
  else:
    print("Cool color!")
print("I don't like red")'''

print("Fill in the blank lyrics!\n(Type in the blank lyrics and see if you are as cool as me.)")
turn=0
print("Never going to ______ you up.")
while True:
  option = input("Enter the missing word: ")
  if option == "give":
    turn += 1
    print("Well done! It only took you", turn, "attempts.")
    break
  else:
    turn += 1
