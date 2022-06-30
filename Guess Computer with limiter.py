import random

def Guess(x):
 print(f"You have 5 chances to guess a number between 1 & {x}" )
 rand = random.randint(1,x)
 guess = 0
 i = 5
 while guess != rand and i>0:
  
  guess = int(input(f'Guess a number between 1 and {x} - '))
  
  if guess < rand and i !=0: 
   print("Try again. Try higher")
   i=i-1
   print(f"You have {i} chances")
   
  
  elif guess > rand and i !=0:
   print("Try again. Try lower")
   i=i-1
   print(f"You have {i} chances")
   
   
 if i == 0:
    print("Sorry! Better luck next time")
 else:   
  print(f"You got it right!! {guess} is the right answer.")

Guess(15)
