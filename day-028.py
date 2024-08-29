'''import random
def character():
  name = input("Enter your character: ")
  type = input ("Character Type (Human, Elf, Wiard, Orc):")
  return name

def calc():
  six = random.randint(1,6)
  twelve = random.randint(1,12)
  health = ((six * twelve) / 2) + 10
  strength = ((six * twelve) / 2) + 12
  print ("HEALTH: ", health)
  print ("STRENGTH", strength)
  print ("May your name go down in Legend...")

character()
calc()'''

'''import random, os, time
def dice(side):
  result = random.randint(1, side)
  return result

def health():
  healthstat = ((dice(6) * dice(12)) / 2) + 10
  return healthstat

def strength():
  strengthstat = ((dice(6) * dice(12)) / 2) + 12
  return strengthstat

name1 = input("Enter your character: ")
type1 = input ("Character Type (Human, Elf, Wiard, Orc):")
health1 = health()
strength1 = strength()
print ("HEALTH: ", health1)
print ("STRENGTH", strength1)

print("Who are they battling?")

name2 = input("Enter your character: ")
type2 = input ("Character Type (Human, Elf, Wiard, Orc):")
health2 = health()
strength2 = strength()
print ("HEALTH: ", health2)
print ("STRENGTH", strength2)

round = 1
while True:
  dice1 = random.randint(1,6)
  dice2 = random.randint(1,6)
  
  difference = abs(strength1 - strength2) + 1

  print("Round", round, "begins!")

  if dice1 > dice2:
    health2 -= difference
    print(name1, "attacks", name2, "for", difference, "damage!")
    round += 1
    if health2 <= 0:
      print(name1, "is the winner! ", round, "rounds!")
      break

  elif dice2 < dice1:
    health1 -= difference
    print(name2, "attacks", name1, "for", difference, "damage!")
    round += 1
    if health1 <= 0:
      print(name2, "is the winner after", round, "rounds!")
      break

  else:
    continue

  print(name1)
  print("HEALTH:", health1)
  print(name2)
  print("HEALTH:", health2)

  time.sleep(5)'''

import random, os, time

def rollDice(side):
  result = random.randint(1,side)
  return result

def health():
  healthStat = ((rollDice(6)*rollDice(12))/2)+10
  return healthStat

def strength():
  strengthStat = ((rollDice(6)*rollDice(8))/2)+12
  return strengthStat


print("⚔️ BATTLE TIME ⚔️")
print()
c1Name = input("Name your Legend:\n")
c1Type = input("Character Type (Human, Elf, Wizard, Orc):\n")
print()
print(c1Name)
c1Health = health()
c1Strength = strength()
print("HEALTH:", c1Health)
print("STRENGTH:", c1Strength)
print()
print("Who are they battling?")
print()

c2Name = input("Name your Legend:\n")
c2Type = input("Character Type (Human, Elf, Wizard, Orc):\n")
print()
print(c2Name)
c2Health = health()
c2Strength = strength()
print("HEALTH:", c2Health)
print("STRENGTH:", c2Strength)
print()

round = 1
winner = None

while True:
  time.sleep(1)
  os.system("clear")
  print("⚔️ BATTLE TIME ⚔️")
  print()
  print("The battle begins!")

  c1Dice = rollDice(6)
  c2Dice = rollDice(6)

  difference = abs(c1Strength - c2Strength) + 1

  if c1Dice > c2Dice:
    c2Health -= difference
    if round==1:
      print(c1Name, "wins the first blow")
    else:
      print(c1Name, "wins round", round)
  elif c2Dice > c1Dice:
    c1Health -= difference
    if round==1:
      print(c2Name, "wins the first blow")
    else:
      print(c2Name, "wins round", round)
  else:
    print("Their swords clash and they draw round", round)

  print()
  print(c1Name)
  print("HEALTH:", c1Health)
  print()
  print(c2Name)
  print("HEALTH:", c2Health)
  print()

  if c1Health<=0:
    print(c1Name, "has died!")
    winner = c2Name
    break
  elif c2Health<=0:
    print(c2Name, "has died!")
    winner = c1Name
    break
  else:
    print("And they're both standing for the next round")
    round += 1


time.sleep(1)
os.system("clear")
print("⚔️ BATTLE TIME ⚔️")
print()
print(winner, "has won in", round, "rounds")
