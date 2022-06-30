import random

def Guess(x):
 print(f"You have 5 chances to guess a number between 1 & {x}" )
 rand = random.randint(1,x)
 guess = 0
 while guess != rand:
  
  guess = int(input(f'Guess a number between 1 and {x} - '))
  
  if guess < rand : 
   print("Try again. Try higher")
 
  elif guess > rand :
   print("Try again. Try lower")
  
 print(f"You got it right!! {guess} is the right answer.")

Guess(15)
