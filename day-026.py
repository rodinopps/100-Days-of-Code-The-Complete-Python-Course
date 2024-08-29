'''import os
for i in range(1,1000):
  print(i)
  os.system("clear")'''

'''import os
print("Welcome")
print("to")
print("Replit")

os.system("clear")

username = input("Username: ")

import os, time
time.sleep(1)
os.system("clear")'''

'''import os
import time

import pygame

pygame.init()
pygame.mixer.init()
sound = pygame.mixer.Sound('audio.wav')
sound.play()

def pause():
  pygame.mixer.pause()

pause()

def play():
  # Play the sound
  pygame.mixer.unpause()
  while True:
    # Start taking user input and doing something with it
    input("Press 2 anytime to pause playback and go back to the menu: ")

while True:
  # clear the screen 
  os.system("clear")

  # Show the menu
  choice = input("🎵 MyPOD Music Player\nPress 1 to Play\nPress 2 to Exit\nPress anything else to see the menu again.")
  if choice == 1:
    play()
  elif choice == 2:
    exit()
  else:
    continue
  
  # take user's input

  # check whether you should call the play() subroutine depending on user's input
  if True:
    play()'''

import os
import time

import pygame

pygame.init()
pygame.mixer.init()
sound = pygame.mixer.Sound('audio.wav')
sound.play()
pygame.mixer.pause()

def pause():
  pygame.mixer.pause()

pause()

def play():
  # Play the sound
  pygame.mixer.unpause()
  while True:
    stop_playback = int(
        input("Press 2 anytime to pause playback and go back to the menu: "))
    if stop_playback == 2:
      pause()
      return  # let's go back from this play() subroutine
    else:
      continue

while True:
  os.system("clear")
  print("🎵 MyPOD Music Player ")
  time.sleep(1)
  print("Press 1 to Play")
  print("Press 2 to Exit")
  print("Press anything else to see the menu again")
  userInput = int(input())
  if userInput == 1:
    print("Playing some proper tunes!")
    play()
  elif userInput == 2:
    exit()
  else:
    continue
