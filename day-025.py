'''#subroutine has parameter called `number`
#`number` shows how many numbers we want the pin to have
def pinPicker(number):
  import random
  pin = "" #this is the empty string
  for i in range(number): #for loop shows defined amount of random numbers
    pin += str(random.randint(0,9)) #we want a string of random numbers between 0-9
  return pin

myPin = pinPicker(4)
print(myPin)'''

'''def areaOfTriangle(base, height):
  area = 0.5 * base * height
  return area

test = areaOfTriangle (5, 22)
print(test)'''

'''def areaOfTriangle(base, height):
  area = 0.5 * base * height
  return area

area = areaOfTriangle (5, 22)
print(area)'''

'''def area_square(side1, side2):
  area = side1 * side2
  return area

area = area_square(4, 12)
print(area)'''

import random

def dice(sides):
  number = random.randint(1, sides)
  return number

def numberdice():
  six = random.randint(1,6)
  eight = random.randint(1,8)
  total = six * eight
  print (total, "hp for your character. ")

while True:
  name = input("Name your warrior: ")
  numberdice()
    
    


  
