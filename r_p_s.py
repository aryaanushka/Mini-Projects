import random

def play():
        user=input(" What's your choice?  'rock' ,'paper' or 'scissor'\n")
        computer=random.choice(['rock','paper','scissor'])
        print(f"The computer's choice is:{ computer}")

        if user==computer:
          return 'It is a tie'
    

        if is_win(user,computer):
         return 'You won!'

        return 'You lost'    
 

def is_win(player,opponent):
    if(player=="rock" and opponent=="paper") or (player=="scissor" and opponent=="paper") or (player=="paper" and opponent=="rock"):
        return True

print(play())
