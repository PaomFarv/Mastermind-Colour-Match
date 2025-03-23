import random
from colorama import Fore
import os

colors = ["R","G","B","Y","O","P","C"]

comp_pick = []

for i in range(4):
    comp_pick.append(random.choice(colors))
#print(comp_pick) for hint purpose.
score = 0

print()
print(Fore.LIGHTRED_EX + "^"*170)
print(Fore.LIGHTGREEN_EX + "Welcome to Mastermind Colour Match.")
os.system('powershell -Command "Add-Type –AssemblyName System.Speech; '
          '$speak = New-Object System.Speech.Synthesis.SpeechSynthesizer; '
          '$speak.Speak(\'Welcome to Mastermind Colour Match.\');"')

input("Press ENTER to continue...")
print(Fore.LIGHTBLUE_EX +"\nYou have to guess 4 colours using their first letters separated by spaces.")
os.system('powershell -Command "Add-Type –AssemblyName System.Speech; '
          '$speak = New-Object System.Speech.Synthesis.SpeechSynthesizer; '
          '$speak.Speak(\'You have to guess 4 colours using their first letters separated by spaces.\');"')

input("Press ENTER to continue...")
print("\nHere are all the colours used in this game: 'R' (Red),'G' (Green),'B' (Blue),'Y' (Yellow),'O' (Orange),'P' (Purple),'C' (Cyan).")
os.system('powershell -Command "Add-Type –AssemblyName System.Speech; '
          '$speak = New-Object System.Speech.Synthesis.SpeechSynthesizer; '
          '$speak.Speak(\'Here are all the colours used in this game:\');"')

input("Press ENTER to continue...")
print("\nYou have 10 attempts to guess the correct colours in the correct order.")
os.system('powershell -Command "Add-Type –AssemblyName System.Speech; '
          '$speak = New-Object System.Speech.Synthesis.SpeechSynthesizer; '
          '$speak.Speak(\'You have 10 attempts to guess the correct colours in the correct order.\');"')

input("Press ENTER to continue...")
print("\nSymbols used to represent -\n'✅ ' denotes correct position, '⚠️ ' correct guess but wrong position, '❌ ' wrong guess.")
os.system('powershell -Command "Add-Type –AssemblyName System.Speech; '
          '$speak = New-Object System.Speech.Synthesis.SpeechSynthesizer; '
          '$speak.Speak(\'Symbols used to represent -\');"')


print(Fore.LIGHTRED_EX + "^"*170)

attempts = 10

def mastermind():
    global attempts,score
    while attempts > 0:
        print(f"Your Score: {score}")
        user_guess = input(Fore.YELLOW+"\nEnter your guess here (spaces in between): ").strip().upper()
        user_pick = user_guess.split(" ")

        if user_pick == comp_pick:
            print("✅✅✅✅")
            print(Fore.GREEN +"\nCongratulations! You guessed it correctly! +1 Points!\n")
            score += 1
            print(Fore.LIGHTRED_EX + "^"*170)
            break

        correct_idx = 0
        wrong_idx = 0

        for i in range(len(user_pick)):
            if comp_pick[i] == user_pick[i]:
                correct_idx += 1
                print("✅ ", end="")
            
            elif user_pick[i] in comp_pick:
                wrong_idx += 1
                count1 = comp_pick.count(user_pick[i])
                count2 = user_pick.count(user_pick[i])

                if count2 > count1:
                    print("❌", end="")
                else:
                    print("⚠️ ", end="")
                
            else:
                wrong_idx += 1
                print(" ❌")
            
        print(Fore.WHITE + f"\nCorrect Position: {correct_idx} | Incorrect Position: {wrong_idx}")

        attempts -= 1
        
        if attempts == 0:
            print(Fore.LIGHTRED_EX +"\nGAME OVER!")
            print(Fore.LIGHTGREEN_EX + "\nCorrect Guess:")
            print(" ".join(comp_pick))

        print(Fore.RED +f"\nYou have {attempts} attempts left.\n")
        print(Fore.LIGHTRED_EX + "^"*170)

while True:
    print(Fore.GREEN + "\nEnter 'Y' to play or 'Q' to quit.\n")
    user_choice = input(Fore.YELLOW + "Enter your response here: ").strip().upper()

    if user_choice == "Y":
        attempts = 10
        mastermind()
        continue
    elif user_choice == 'Q':
        print(Fore.LIGHTRED_EX +"You Have Exited From The Game. GoodBye!\n")
        print(Fore.LIGHTRED_EX + "^"*170)
        break
    else:
        print(Fore.LIGHTRED_EX +"Invalid Response, Please Try Again.")

