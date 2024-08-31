import random 
listOfWords = ["british", "suave", "integrity", "accent", "evil", "genius", "Downton"]
wordChosen = random.choice(listOfWords)

turns = 10
used = []

while True:
  letter = input("Choose a letter: ").lower()
  if letter in used:
    print("You have used that letter already. ")
  used.append(letter)

  if letter in wordChosen:
    print(" You found a letter. ")
  else:
    print(" Not a letter in the word. ")
    turns -= 1

  all = True
  for i in wordChosen:
    if i in used:
      print(i, end = "")
    else:
      print("_", end = "")
      all = False

  if all:
    print(f" You won with {turns} left!")
    break

  if turns == 0:
    print(f"You ran out of lives! The answer was {wordChosen}")
    break
  else:
    print(f"Only {turns} left")
      