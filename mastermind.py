import random
from colorama import Fore

colors = ["R","G","B","Y","O","P","C"]

comp_pick = []

for i in range(4):
    comp_pick.append(random.choice(colors))
print(comp_pick)
#print(comp_pick) for hint purpose.

print()
print(Fore.LIGHTRED_EX + "^"*100)
print(Fore.LIGHTGREEN_EX + "Welcome to Mastermind Colour Match.")
input("Press ENTER to continue...")
print(Fore.LIGHTBLUE_EX +"\nYou have to guess 4 colours using their first letters separated by spaces.")
input("Press ENTER to continue...")
print("\nHere are all the colours used in this game: 'R','G','B','Y','O','P','C'.")
input("Press ENTER to continue...")
print("\nYou have 10 attempts to guess the correct colours in the correct order.")
input("Press ENTER to continue...")
print(Fore.LIGHTRED_EX + "^"*100)

attempts = 10

while attempts > 0:
    user_guess = input(Fore.YELLOW+"\nEnter your guess here (spaces in between): ").strip().upper()
    user_pick = user_guess.split(" ")

    if user_pick == comp_pick:
        print(Fore.GREEN +"\nCongratulations! You guessed it correctly!\n")
        break

    correct_idx = 0
    wrong_idx = 0

    for i in range(len(user_pick)):
        if comp_pick[i] == user_pick[i]:
            correct_idx += 1
        else:
            wrong_idx += 1
        
    print(Fore.WHITE + f"Correct Position: {correct_idx} | Incorrect Position: {wrong_idx}")

    attempts -= 1
    
    if attempts == 0:
        print(f"GAME OVER!")

    print(Fore.RED +f"You have {attempts} attempts left.\n")

