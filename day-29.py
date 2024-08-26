'''for i in range(0, 100):
  print(i, end=" ")'''

'''for i in range(0, 100):
  print(i, end=", ")'''

'''#new line
for i in range(0, 100):
  print(i, end="\n")'''

'''#tab indent
for i in range(0, 100):
  print(i, end="\t")'''

'''#vertical tab
for i in range(0, 100):
  print(i, end="\v")'''

'''print("If you put")
print("\033[33m", end="") #yellow
print("nothing as the")
print("\033[35m", end="") #purple
print("end character")
print("\033[32m", end="") #green
print("then you don't")
print("\033[0m", end="") #default
print("get odd gaps")

print("If you put", "\033[33m", "nothing as the", "\033[35m", "end character", "\033[32m", "then you don't", "\033[0m", "get odd gaps", end="")'''

'''import os

for i in range(1, 101):
  print(i)
  os.system("clear")'''

'''import os, time

for i in range(1, 101):
  print(i)
  time.sleep(0.5)
  os.system("clear")'''

'''import os, time
print('\033[?25l', end="")
for i in range(1, 101):
  print(i)
  time.sleep(0.2)
  os.system("clear")'''

def text(colour, word):
  if colour == "yellow":
    print("\033[33m", word, sep = "", end = "")
  elif colour == " pink":
    print("\033[35m", word, sep = "", end = "")
  elif colour == "red":
    print("\033[31m", word, sep = "", end ="")
  elif colour == "cyan":
    print("\033[0;36m", word, sep = "", end = "")

text("yellow", "Super Subroutine")
print()
print("With my ", end="")
text("red", "new program")
text("reset", " I can just call red('and') ")
text("red", " it will print in red ")
text("cyan", "or even blue")