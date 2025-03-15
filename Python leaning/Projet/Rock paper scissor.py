import random

option = ["rock", "paper", "scissor"]

print("Lets play Rock Paper Scissor\n\n What do you want to pick")

player = input("\n 1. rock\n 2. paper\n 3. scissor\n").lower()
pc = random.choice(option)

if player == "1":
    player = "rock"
elif player == "2":
    player = "paper"
elif player == "3":
    player = "scissors"
elif player not in option:
    print("Please choose 1, 2 or 3. You can also write your choice, like scissor")
    exit()

if player == "rock" and pc == "rock":
    print("Its a tie")

elif player == "rock" and pc == "paper":
    print("you loose")

elif player == "rock" and pc == "scissor":
    print("you win")

elif player =="paper" and pc == "rock":
    print("you win")

elif player == "paper" and pc == "paper":
    print("Its a tie")

elif player == "paper" and pc == "scissor":
    print("you loose")

elif player == "scissor" and pc == "rock":
    print("you loose")

elif player == "scissor" and pc == "paper":
    print("you win")

elif player == "scissor" and pc == "scissor":
    print("its a tie")

print(f"the computer played {pc}")