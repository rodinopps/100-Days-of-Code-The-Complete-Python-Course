def change(colour):
  if colour == "red":
    return ("\033[31m")
  elif colour=="white":
    return ("\033[0m")
  elif colour=="blue":
    return ("\033[34m")
  elif colour=="yellow":
    return ("\033[33m")
  elif colour == "green":
    return ("\033[32m")
  elif colour == "purple":
    return ("\033[35m")

title = f"{change('red')}={change('white')}={change('blue')}= {change('yellow')}Music App {change('blue')}={change('white')}={change('red')}="

print(f"        {title:^35}")
print(f"🔥▶️\t{change('white')}Radio Gaga")
print(f"\t{change('yellow')}Queen")

prev = "prev"
next = "next"
pause = "pause"
print(f"{change('white')}{prev:<35}")
print(f"{change('green')}{next:^35}")
print(f"{change('purple')}{pause:>35}")
print()
print()
text = "WELCOME TO"
print(f"{change('white')}{text:^35}")
text = "--  ARMBOOK  --"
print(f"{change('blue')}{text:^35}")
text = "Definitely not a rip off"
print(f"{change('yellow')}{text:>35}")
text = "a certain other social"
print(f"{change('yellow')}{text:>35}")
text = "networking site"
print(f"{change('yellow')}{text:>35}")
text = "Honest."
print(f"{change('red')}{text:^35}")
text = "Username: "
username = input(f"{change('white')}{text:^35}")
text = "Password: "
username = input(f"{change('white')}{text:^35}")
