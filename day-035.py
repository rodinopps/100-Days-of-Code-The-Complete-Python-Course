import os, time
list = []
def choice():
  option = input("Do you want to view, add, edit, remove an item from the to do list or delete the list?\n")
  
  if option == "view":
    print()
    for i in list:
      print(i)
    print()
    
  elif option == "add":
    task = input("What do you want to add?\n")
    if task in list:
      print("You have already added this to the list. ")
    else:
      list.append(task)

  elif option == "remove":
    delete = input("What do you want to delete?\n")
    confirm = input("Are you sure you want to remove this?\n")
    if confirm == "yes":
      list.remove(delete)
      
  elif option == "delete":
    list.clear()
    
  elif option == "edit":
    item = input("What do you want to edit?\n")
    if item in list:
      change = input("What do you want to change it to? ")
      if change in list:
        print("You have already added this to the list. ")
      else:
        index = list.index(item)
        list[index] = change
        
  time.sleep(1)
  os.system("clear")

while True:
  choice()
