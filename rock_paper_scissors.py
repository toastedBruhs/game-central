import random

print("Welcome to Rock, Paper, Scissors!")
compchoices = ["rock", "paper", "scissors"]
userSel = input("Please choose rock, paper, or scissors: ")
compSel = random.choice(compchoices)
if userSel != "rock" or "paper" or "scissors":
    print("That is not a valid choice.")
if userSel == compSel:
    print("It's a tie!")
elif userSel == "rock":
    if compSel == "paper":
        print("I win!")
    else:
        print("You win!")
elif userSel == "paper":
    if compSel == "scissors":
        print("I win!")
    else:
        print("You win!")
elif userSel == "scissors":
    if compSel == "rock":
        print("I win!")
    else:
        print("You win!")
print("You chose " + userSel + " and I chose " + compSel + ".")