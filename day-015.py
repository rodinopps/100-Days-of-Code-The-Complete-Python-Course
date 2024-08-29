'''counter = 0
while counter < 10:
  print(counter)
  counter +=1'''

'''counter = 0
while counter < 101:
  print(counter)
  counter +=1'''

'''counter = 0
while counter < 10:
  print(counter)
  counter += 1'''

'''counter = 0
while counter < 6:
  print(counter)
  counter += 1'''

'''exit = ""
while exit != "yes":
  print("🥳")
  exit = input("Exit?: ")'''

'''counter = 0
while counter < 25:
  print(counter)
  counter += 1'''

'''counter = 0
while counter <= 12:
  print(counter)
  counter += 1'''

'''exit = ""
while exit != "yes":
  print("🥳")
  exit = input("Exit?: ")'''

x = 0
while x == 0:
  option = input("What animal do you want?: ")
  if option == "Cow" or option == "cow":
    print("A cow goes moo. ")
  elif option == "Chicken" or option == "chicken":
    print("A chicken goes cluck. ")
  else:
    print("???")
  exit = input("Do you want to exit? ")
  if exit == "yes" or exit == "Yes":
    x += 1
  
