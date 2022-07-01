
import random
def play():
    user = ('r' , 'p' , 's')
    computer = ('r' , 'p' , 's')
    print("Lets play rock papper sissors...")
    print("s for sisssors, p for paper and r for rock")
    pl = 0
    op = 0 
    while score(pl,op) == True:
        computer = random.choice(['r','p','s'])
        user = input("Choose Rock, paper or Sissor: ")
        print("Computers choice -- " + computer)
        if (user == computer):
                print("its a tie")
                
        elif (win(user,computer)):
                print("You won")
                pl = pl + 1
                print(f"score = {pl}:{op}")
        else:
                print("You lost")
                op = op + 1
                print(f"score = {pl}:{op}")
    final(pl,op)
    


def win(pl, op):
 # p>>r, r>>s, s>>p, 
 if (pl == 'p' and op == 'r') or (pl == 'r' and op == 's') or (pl == 's' and op == 'p'):
    return True

def score(x,y):
    if x<5 and y<5:
     return True
    
    else:
        return False 

def final(a,b):
    if a>b:
        print("Yay! You Won! Congrats")
    else:
        print("Better luck next time!")    


play()