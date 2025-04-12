import random
import time


# Prints a message and pauses for a specified amount of time
# The default is 2 seconds
def print_pause(message_to_print, delay=2):
    print(message_to_print)
    time.sleep(delay)


# Prepares the initial game state
# Sets the initial values for cave_visited, weapon, and enemy
# The enemy is randomly chosen from a list of enemies
# Returns the state as a dictionary
def prepare_state():
    cave_visited = False
    weapon = 'dagger'
    enemies = ['troll', 'wicked fairie', 'pirate', 'gorgon', 'dragon']
    enemy = random.choice(enemies)
    state = {
        'cave_visited': cave_visited,
        'weapon': weapon,
        'enemy': enemy
    }
    return state


# The main function that starts the game
def play_game(state):
    print_pause("==================================\n"
                "= Welcome to the Adventure Game! =\n"
                "==================================\n")
    print_pause("In this game, you will explore a mysterious land.")
    print_pause("You will encounter various challenges and make choices "
                "that will affect the outcome of your adventure.\n")
    print_pause("Are you ready to begin? (y/n)", 0)
    choice = ""
    while choice not in ['y', 'n']:
        choice = input().lower()
        if choice == 'y':
            print_pause("\nGreat! Let's get started!\n")
            field(state)
        elif choice == 'n':
            print_pause("", 0)
            end_game()
        else:
            print_pause("Sorry, I don't understand.")
            print_pause("Please enter y or n.", 0)


# Step 1: The player starts in a field
def field(state):
    print_pause("You find yourself standing in an open field, "
                "filled with grass and yellow wildflowers.")
    print_pause(f"Rumor has it that a {state['enemy']} is somewhere around "
                "here, and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause(f"In your hand you hold your trusty {state['weapon']}.\n")
    where_to_go(state)


# Step 2: The player chooses where to go: house or cave
def where_to_go(state):
    print_pause("What would you like to do?", 0)
    print_pause("Enter 1 to knock on the door of the house.", 0)
    print_pause("Enter 2 to peer into the cave.", 0)
    response = ""
    while response not in ['1', '2']:
        response = input().lower()
        if response == '1':
            print_pause("", 0)
            house(state)
        elif response == '2':
            print_pause("", 0)
            cave(state)
        else:
            print_pause("Sorry, I don't understand.")
            print_pause("Please enter 1 or 2.", 0)


# Step 3a: The player chooses to enter the house
def house(state):
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door opens..")
    print_pause(f"And out steps a {state['enemy']}!!", 3)
    print_pause(f"Eep! This is the {state['enemy']}'s house!")
    print_pause(f"The {state['enemy']} attacks you!!\n")
    combat(state)


# Fight with the enemy
# The player can choose to fight or run away
# If the player chooses to fight, the outcome is determined by the weapon
# If the player has a sword, he/she always wins
# If the player has another weapon, he/she needs luck to win
def combat(state):
    if state['weapon'] == 'dagger':
        print_pause("You feel a little under-prepared for this, "
                    f"what with only having a tiny {state['weapon']}.\n")
    print_pause("Would you like to fight (1) or run away (2)?", 0)
    choice = ""
    while choice not in ['1', '2']:
        choice = input().lower()
        if choice == '1':
            if state['weapon'] == 'sword':
                print_pause("", 0)
                print_pause(f"If the {state['enemy']} moves to attack, "
                            "you unsheath your sword.")
                print_pause("The sword of Ogoroth shines brightly "
                            "in your hand as you brace yourself.")
                print_pause(f"But the {state['enemy']} takes one look at your "
                            "shiny new toy and runs away!")
                print_pause(f"You have rid the town of the {state['enemy']}. "
                            "You are victorious!\n", 3)
                game_over('won')
            else:
                print_pause("", 0)
                print_pause("You do your best...\n", 4)
                luck = random.randint(1, 6)
                if luck < 5:
                    print_pause(f"But your {state['weapon']} is no match for "
                                f"the {state['enemy']}.")
                    print_pause("You have been defeated!\n", 3)
                    game_over('lost')
                else:
                    print("You got lucky and defeated the enemy!!\n", 3)
                    game_over('won')
        elif choice == '2':
            print_pause("", 0)
            print_pause("You run back into the field. "
                        "Luckily, you don't seem to have been followed.\n")
            where_to_go(state)
        else:
            print_pause("Sorry, I don't understand.")
            print_pause("Please enter 1 or 2.", 0)


# Step 3b: The player chooses to enter the cave
def cave(state):
    print_pause("You peer cautiously into the cave.\n")

    if state['cave_visited']:
        print_pause("You've been here before, and gotten all the good stuff. "
                    "It's just an empty cave now.")
    else:
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical sword of Ogoroth!")
        print_pause(f"You discard your silly old {state['weapon']} and "
                    "take the sword with you.")
        state['weapon'] = 'sword'
        state['cave_visited'] = True
    print_pause("", 0)
    print_pause("You walk back out to the field.\n")
    where_to_go(state)


# Step 4: The game is finished
def game_over(result):
    print_pause(f"You {result} the game!!\n")
    print_pause("Game Over!\n")
    print_pause("Would you like to play again? (y/n)", 0)
    play_again()


# Step 5: The player can choose to play again
def play_again():
    choice = ""
    while choice not in ['y', 'n']:
        choice = input().lower()
        if choice == 'n':
            print_pause("", 0)
            end_game()
        elif choice == 'y':
            print_pause("", 0)
            print_pause("Excellent! Restarting the game...\n")
            state = prepare_state()
            play_game(state)
        else:
            print_pause("Sorry, I don't understand.")
            print_pause("Please enter y or n.", 0)


# Step 6: End the program
def end_game():
    print_pause("Thanks for playing! See you next time!")


# Start
# Initialize the game state
state = prepare_state()
# Play the game
play_game(state)
