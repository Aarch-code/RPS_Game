import random

n = input("Enter your Name: ")
print(f"Hello {n}, Welcome to the Game of Rock, Paper, Scissor. \n Press r fo Rock, p for Paper and s for Scissor")

lst = ["r", "p", "s"]

chance = 10
no_of_chance = 0
human_point = 0
computer_point = 0

while no_of_chance < chance:
    _input = input("Rock, Paper, Scissor: ")
    _random = random.choice(lst)

    if _input == _random:
        print("Game is Tie, both get 1 point each \n ")
        computer_point = computer_point + 1
        human_point = human_point + 1
        print(f"computer_point is {computer_point} and your point is {human_point} \n ")

    # if user enter r

    elif _input == "r" and _random == "p":
        computer_point = computer_point + 1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("computer wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n ")

    elif _input == "r" and _random == "s":
        human_point = human_point + 1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("Human wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n")

    # if user enter p

    elif _input == "p" and _random == "s":
        computer_point = computer_point + 1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("computer wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n ")

    elif _input == "p" and _random == "r":
        human_point = human_point + 1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("Human wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n")

    # if user enter s

    elif _input == "s" and _random == "p":
        human_point = human_point + 1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("Human wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n")


    elif _input == "s" and _random == "r":
        computer_point = computer_point + 1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("computer wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n ")

    else:
        print("your input is invalid. \n")

    no_of_chance = no_of_chance + 1
    print(f"{chance - no_of_chance} chance(s) left out of {chance} chances \n")

print("Game over")

if computer_point == human_point:
    print("Tie")

elif computer_point > human_point:
    print("Computer wins and you lose")

else:
    print("You win and computer lose")

print(f"your point is {human_point} and computer point is {computer_point}")
