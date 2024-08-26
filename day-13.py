test = input("Enter the name of the test: ")
max = int(input("Enter maximum score: "))
score = int(input("Enter score recieved: "))
percent = round(((score/max)*100), 2)

if percent >= 90 and percent <= 100:
  print("A+")
elif percent >= 80 and percent <= 89:
  print("A")
elif percent >= 70 and percent <= 79:
  print("B")
elif percent >= 60 and percent <= 69:
  print("C")
elif percent >= 50 and percent <= 59:
  print("D")
elif percent < 50:
  print("U")
else:
  print("Error. Please try again. ")