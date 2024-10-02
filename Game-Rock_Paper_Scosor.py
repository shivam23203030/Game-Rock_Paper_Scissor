import random
def determine_winner(computer_c,user_c,name):
    if user_c==computer_c:
        return "Tie match !"
    elif(user_c=="rock" and computer_c=="scissor") or (user_c=="paper" and computer_c=="stone") or (user_c=="scissor" and computer_c=="paper"):
        return f"{name} is winner"
    else:
        return "computer is winner"
    
name=input("Enter Player Name :: ")
print(f"----------Hi {name}, WELCOME TO THE GAME----------")
print("---I am your computer,Lets play the game (ROCK-PAPER-SCISSOR)---")
choises=['rock','paper','scissor']
while True:
    computer_c=random.choice(choises)
    user_c=input("Enter your choise (rock,paper,scissor) :: ").lower()
    print(f"Computer's choise is :: {computer_c}")
    winner=determine_winner(computer_c,user_c,name)
    print(f" {winner}")
    choise=input("Do you want to play Again? (Yes/No) :: ").lower()
    if choise=="yes":
        continue
    else:
        exit()

