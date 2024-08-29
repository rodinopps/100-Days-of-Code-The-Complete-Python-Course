'''name = input("What's your name? ")
if name == "David" or name == "david":
  print("Hello Baldy!")
else: 
  print("What a beautiful head of hair!")'''

'''name = input("What's your name? ")
if name.lower() == "david": 
  print("Hello Baldy!")
else: 
  print("What a beautiful head of hair!")'''

'''name = input("What's your name? ")
if name.lower().strip() == "david": 
  print("Hello Baldy!")
else: 
  print("What a beautiful head of hair!")'''

'''myList = []

def printList():
  print()
  for i in myList:
    print(i)
  print()

while True:
  addItem = input("Item > ")
  if addItem not in myList:
    myList.append(addItem) 
  printList()'''

'''myList = []

def printList():
  print()
  for i in myList:
    print(i)
  print()

while True:
  addItem = input("Item > ").strip().capitalize()
  if addItem not in myList:
    myList.append(addItem)
  printList()'''

'''whatToEat = input("What do you fancy for dinner? ")
if whatToEat.strip == "pasta": 
  print("Get out the pasta maker.")
elif whatToEat.strip().lower() == "tacos":
  print("Let's do Taco Tuesday!")
else: 
  print("Go search the fridge.")'''

list = []
def check():
  first = input("Enter your first name.\n").strip().capitalize()
  last = input("Enter your last name.\n").strip().capitalize()
  name = f"{first} {last}"
  if name in list:
    print("ERROR")
  else:
    list.append(name)
  print()
  for i in list:
    print(i)
  print()

while True:
  check()
      
