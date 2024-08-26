'''for i in range(100, 110):
  print(i)'''

'''for i in range(1, 7):
  print("Day", i)'''

'''for i in range(1, 8):
  print("Day", i)'''

'''print("Thirteen Times Table")
for i in range(1, 13):
  print(i, "x 13 =", i * 13)'''

'''for i in range (0, 1000000, 25):
  print(i)'''

'''for i in range(10, -1, -1):
  print(i)'''

'''for i in range (10, 0, -1):
  print(i)'''

'''for i in range (20, 40, 1):
  print(i)'''

start = int(input("Enter a starting number: "))
end = int(input("Enter a ending number: "))
num = int(input("Enter an increment: "))

for i in range(start, end, num):
  print(i)