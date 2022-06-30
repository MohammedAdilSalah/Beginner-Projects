import random
def Guess(x):
 low = 1
 high = x
 feedback = ''
 while feedback != 'c':
    if low != high:
        guess = random.randint(low,high)
    else:
        guess = low
    feedback = input(f"Is {guess} High 'h', low 'l' or correct 'c'? - ")
    if feedback == 'h':
        guess - 1
    else:
        guess + 1

 print("Computer guessed it right!!")

Guess(10)
  