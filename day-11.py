minute = 60
hour = 60
day = 24
choice = int(input("How many days in the year? "))
if choice == 365:
  print(choice * day * hour * minute)
elif choice == 366:
  print(choice * day * hour * minute)
else:
  print("Error. Please try again. ")