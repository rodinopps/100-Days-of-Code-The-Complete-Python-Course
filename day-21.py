score = 0
choice = int(input("Name your multiples: "))
for i in range(10):
  print(i+1, "X", choice, "= ")
  answer = int(input("Enter the answer: "))
  if answer == (i+1)*choice:
    print("Great work!")
    score += 1
  elif answer != (i+1)*choice:
    print("No the answer is", (i+1)*choice)

print(score)
