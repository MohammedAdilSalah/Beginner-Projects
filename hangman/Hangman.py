import random
from Words import words
import string
from HangmanVisual import visual   

def Word_Selection():
    chosen = random.choice(words)
    while ' ' or '-' in chosen:
        chosen = random.choice(words)
        return (chosen).upper()

def user_input():
    
    word= Word_Selection()
    i = 7
    wordset = set(word)
    usedword= set()
    alphabet = set(string.ascii_uppercase)
    #print(alpha," ", wordset," ",usedword)
    #print(word)
    #print(len(wordset))
    while len(wordset) > 0 and i>0:
        print("Letters guessed so far:"," ".join(usedword))
        wordlist = [letter if letter in usedword else '_' for letter in word]
        print(wordlist)
        alpha = input("Type a letter: ").upper()
        if alpha in usedword and alpha in alphabet:
            print("You have already guessed it")
           
        elif alpha in alphabet:
             usedword.add(alpha)
             if alpha in wordset:
                 wordset.remove(alpha)
             else:
                i=i-1
                print (visual(i))
                print (f"remaing lives = {i}")
        else:
            print("Invalid character! Keep trying.")
    if len(wordset) == 0:
        print (f"Wow! You guessed it.{word} is the right!")
    else:
        print("Sorry!!! Out of lives")
        print(f"The correct word is {word}")
# print(Word_Selection())
user_input()



    

