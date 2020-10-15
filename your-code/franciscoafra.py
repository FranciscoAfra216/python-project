#COINFLIP
import random
def play_room(room):
    """
    Play a room. First check if the room being played is the target room.
    If it is, the game will end with success. Otherwise, let player either
    explore (list all items in this room), examine an item found here or talk to someone.
    """
    game_state["current_room"] = room
    if (game_state["current_room"] == game_state["target_room"]):
        print("Congrats! You escaped the room!")
    else:
        print("\nYou are now in " + room["name"], "\n")
        intended_action = input("What would you like to do? Type 'explore', 'examine' or 'talk'?").strip()
        if intended_action == "explore":
            explore_room(room)
            play_room(room)
        elif intended_action == "examine":
            examine_item(input("What would you like to examine?").strip())
        elif intended_action == "talk":
            talk_to(input("Who would you like to talk with?").strip())
        else:
            print("Not sure what you mean. Type 'explore', 'examine' or 'talk'.")
            play_room(room)
        linebreak()

def coin_toss():
    door_e = {
        "name": "door e",
        "type": "door",
        "riddle": "none"
    }

    key_e = {
        "name": "key for door e",
        "type": "key",
        "target": door_e,
    }


    player_choice = input("It's time to flip a coin!\nChoose heads or tails?")
    player_choice = player_choice.lower()
    while player_choice != "heads" and player_choice != "tails":
        player_choice = input("Please, pick heads or tails!")
        player_choice = player_choice.lower()

    coinflip = random.choice(["heads", "tails"])
    print("You picked", player_choice + ".")
    print("Alright, let's flip it!\n")
    print("You were so scared. That you see the coin flipping in slow motion!\n")
    print("The coin showed", coinflip+"!\n")

    if player_choice == coinflip:
        print("Good job, here is the key e!")
        play_room(current_room)
        return key_e

    else:
        print("Sadly, You guessed wrong!\n")


def bullet_position():
    bullet_position = random.randrange(1, 6, 1)
    return bullet_position


def spin_chamber():
    chamber_position = random.randrange(1, 6, 1)
    return chamber_position


# bullet_position + spin_chamber
def fire_gun():
    rounds = 1
    print("Round:", rounds)
    if rounds < 2:
        if bullet_position() == spin_chamber():
            return "You´re dead. GAME OVER!"
        else:
            return key_a
