'''adding = 4 + 3
print(adding)

subtraction = 8 - 9
print(subtraction)

multiplication = 4 * 32
print(multiplication)

division = 50 / 5
print(division)

# a number raised to the power of some number
# in this example we raise 5 to the power of 2
squared = 5**2
print(squared)

# remainder of a division
modulo = 15 % 4
print(modulo)

# whole number division
divisor = 15 // 2
print(divisor)'''

'''# Solve the following problems with my code
# Your goal is to print the solution of all 3 calculations to the screen.

# multiplication
print(3.4 * 6.8)

# division
print(2467 / 4673)

#raise 10 to the power of 2
print(10**3)

# print the remainder when 343 is divided by 4
print(343 // 100)'''

'''myBill = float(input("What was the bill?: "))
tip = int(input("What % of tip?"))
numberOfPeople = int(input("How many people?: "))
answer = myBill / numberOfPeople
answer = round(answer, 2)
print("You all owe", answer)'''

myBill = float(input("What was the bill?: "))
numberOfPeople = int(input("How many people?: "))
tip = int(input("What % of tip?"))
total = myBill + tip/100 * myBill
answer = total / numberOfPeople
answer = round(answer, 2)
print("You all owe", answer)
