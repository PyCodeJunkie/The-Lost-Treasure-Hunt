import os
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def press_to_continue():
    print("Press enter to continue...")
    input()

def show_help():
    clear_screen()
    print("Welcome to the Help section!\n")
    print("The objective of this game is to make choices and progress through the story.\n")
    print("You will be presented with different options to choose from and your choices will determine the outcome of the game.\n")
    print("You can type 'hint' at any time during the game to get a hint on what to do next.\n")
    print("Good luck and have fun!\n")
    press_to_continue()

def show_hint():
    clear_screen()
    print("Here is a hint to help you progress in the game:\n")
    print("Think carefully before making a choice, as it may impact the outcome of the game.\n")
    press_to_continue()

def start_game():
    clear_screen()
    print("Welcome to the Adventure Game!\n")
    print("You find yourself in a mysterious place with no memory of how you got there.\n")
    print("You see two paths in front of you, one leading to the left and the other to the right.\n")
    print("Which path do you take?\n")
    print("1. Left")
    print("2. Right")
    choice = input("Enter your choice: ")
    if choice == "1":
        left_path()
    elif choice == "2":
        right_path()
    else:
        print("Invalid choice, try again.")
        press_to_continue()
        start_game()

def left_path():
    clear_screen()
    print("You chose the path to the left.\n")
    print("As you walk down the path, you come across a fork in the road.\n")
    print("You see a sign pointing to the left that says 'Treasure lies ahead.'")
    print("And another sign pointing to the right that says 'Danger ahead.'")
    print("Which path do you take?\n")
    print("1. Left")
    print("2. Right")
    choice = input("Enter your choice: ")
    if choice == "1":
        treasure()
    elif choice == "2":
        danger()
    else:
        print("Invalid choice, try again.")
        press_to_continue()
        left_path()

def right_path():
    clear_screen()
    print("You chose the path to the right.\n")
    print("As you walk down the path, you come across a bridge.\n")
    print("You see a sign that says 'Cross the bridge to reach safety.'")
    print("But as you take a closer look, you notice that the bridge is damaged and might collapse.\n")
    print("What do you do?\n")
    print("1. Cross the bridge")
    print("2. Turn back")
    choice = input("Enter your choice: ")
    if choice == "1":
        cross_bridge()
    elif choice == "2":
        turn_back()
    else:
        print("Invalid choice, try again.")
        press_to_continue()
        right_path()

def treasure():
    clear_screen()
    print("You found the treasure!\n")
    print("Congratulations, you have completed the game.\n")
    print("Thanks for playing.")
    press_to_continue()
    exit()

def danger():
    clear_screen()
    print("You encountered danger and were unable to complete the game.\n")
    print("Better luck next time.")
    press_to_continue()
    exit()

def cross_bridge():
    clear_screen()
    print("You successfully crossed the bridge and reached safety.\n")
    print("Congratulations, you have completed the game.\n")
    print("Thanks for playing.")
    press_to_continue()
    exit()

def turn_back():
    clear_screen()
    print("You decided to turn back and return to the starting point.\n")
    print("Do you want to try a different path?\n")
    print("1. Yes")
    print("2. No")
    choice = input("Enter your choice: ")
    if choice == "1":
        start_game()
    elif choice == "2":
        print("Thanks for playing.")
        exit()
    else:
        print("Invalid choice, try again.")
        press_to_continue()
        turn_back()

def main_menu():
    clear_screen()
    print("Welcome to the Adventure Game!\n")
    print("1. Start Game")
    print("2. Help")
    print("3. Quit")
    choice = input("Enter your choice: ")
    if choice == "1":
        start_game()
    elif choice == "2":
        show_help()
    elif choice == "3":
        print("Thanks for playing.")
        exit()
    else:
        print("Invalid choice, try again.")
        press_to_continue()
        main_menu()

if __name__ == "__main__":
    while True:
        main_menu()

