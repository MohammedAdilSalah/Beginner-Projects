import random
def play():
    user = ('r' , 'p' , 's')
    computer = random.choice(['r','p','s'])
    print("Lets play rock papper sissors...")
    print("s for sisssors, p for paper and r for rock")
    user = input("Choose Rock, paper or Sissor: ")
    
    if (user == computer):
        print("its a tie")
        
    elif (win(user,computer)):
        print("You won")
        
    else:
        print("You lost")
        
    print (f"Computers choice - {computer}")


def win(pl, op):
 # p>>r, r>>s, s>>p, 
 if (pl == 'p' and op == 'r') or (pl == 'r' and op == 's') or (pl == 's' and op == 'p'):
    return True

play()