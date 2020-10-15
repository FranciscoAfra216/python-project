#COINFLIP
import random
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
    print("Alright, let's flip it!")
    print("You were so scared. That you see the coin flipping in slow motion!")
    print("The coin showed", coinflip+"!")

    if player_choice == coinflip:
        print("Good job, here is a key!")
        return key_e

    else:
        print("Sadly, You guessed wrong!")
    play_room(current_room)

