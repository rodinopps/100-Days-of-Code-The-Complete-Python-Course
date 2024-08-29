import random
def character():
  name = input("Enter your character: ")
  type = input ("Character Type (Human, Elf, Wiard, Orc):")
  print(name)

def calc():
  six = random.randint(1,6)
  twelve = random.randint(1,12)
  health = ((six * twelve) / 2) + 10
  strength = ((six * twelve) / 2) + 12
  print("HEALTH: ", health)
  print("STRENGTH", strength)
  print("May your name go down in Legend...")

character()
calc()
  
