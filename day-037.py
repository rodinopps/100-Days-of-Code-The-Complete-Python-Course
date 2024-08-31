'''myString = "Hello there my friend."
print(myString[0])

# This code outputs the 'H' from 'Hello'''

'''myString = "Hello there my friend."
print(myString[6:11])

# This code outputs 'there'.'''

'''myString = "Hello there my friend."
print(myString[:11])

# This code outputs 'Hello there'.'''

'''myString = "Hello there my friend."
print(myString[12:])
# This code outputs 'my friend.'.'''

'''myString = "Hello there my friend."
print(myString[5:])

# This code outputs 'Hlo' (every second character from 'Hello').'''

'''myString = "Hello there my friend."
print(myString[::3])

# This code outputs 'Hltrmfe!' (every third character from the whole string).

myString = "Hello there my friend."
print(myString[0:6:2])

# This code outputs 'Hlo' (every second character from 'Hello').'''

'''myString = "Hello there my friend."
print(myString[::-1])

#This code reverses the string, outputting '.dneirf ym ereht olleH'''

'''myString = "Hello there my friend."
print(myString.split())

#This code outputs ['Hello', 'there', 'my', 'friend.']'''

'''myString = "Hello there my friend."
print(myString[0:5])'''

'''myString = "Hello there my friend."
print(myString[0:4:1])'''

'''# This code should output 'Hello there'
myString = "Hello there my friend."
print(myString[0:11:1])'''

'''print("STAR WARS NAME GENERATOR")

questions = input("Enter your first name, last name, Mum's maiden name and the city you were born in").split()

first = questions[0].strip()
last = questions[1].strip()
maiden = questions[2].strip()
city = questions[3].strip()

name = f"{first[:3].title()}{last[:3].lower()} {maiden[:2].title()}{city[-3:].lower()}"'''


print("STAR WARS NAME GENERATOR")

all = input("Enter your first name, last name, Mum's maiden name and the city you were born in").split()

first = all[0].strip()
last = all[1].strip()
maiden = all[2].strip()
city = all[3].strip()

name = f"{first[:3].title()}{last[:3].lower()} {maiden[:2].title()}{city[-3:].lower()}"

print(f"Your Star Wars name is {name}")