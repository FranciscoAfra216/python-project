# function import from contributors
from franciscoafra import coin_toss
import random

lives = []
# define rooms, items and humans/animals
house_owner = {
    "name": "david",
    "type": "human",
    "riddle": "flip coin"
}

gamer_guy = {
    "name": "gamer",
    "type": "human",
    "riddle": "none"
}

cowboy_texas = {
    "name": "cowboy",
    "type": "human",
    "riddle": "gun fire"
}

kid_2 = {
    "name": "sophie",
    "type": "human",
    "riddle": "none"
}

buffon_1 = {
    "name": "buffon",
    "type": "human",
    "riddle": "penalty"
}

spider = {
    "name": "spidey",
    "type": "animal",
    "riddle": "none"
}

couch = {
    "name": "couch",
    "type": "furniture",
    "riddle": "none"
}

piano = {
    "name": "piano",
    "type": "furniture",
    "riddle": "none"
}

double_bed = {
    "name": "double bed",
    "type": "furniture",
    "riddle": "none"
}

dresser = {
    "name": "dresser",
    "type": "furniture",
    "riddle": "none"
}

queen_bed = {
    "name": "queen bed",
    "type": "furniture",
    "riddle": "none"
}

dining_table = {
    "name": "dining table",
    "type": "furniture",
    "riddle": "none"
}

door_a = {
    "name": "door a",
    "type": "door",
    "riddle": "none"
}

door_b = {
    "name": "door b",
    "type": "door",
    "riddle": "none"
}

door_c = {
    "name": "door c",
    "type": "door",
    "riddle": "none"
}

door_d = {
    "name": "door d",
    "type": "door",
    "riddle": "none"
}

door_e = {
    "name": "door e",
    "type": "door",
    "riddle": "none"
}

key_a = {
    "name": "key for door a",
    "type": "key",
    "target": door_a,
}

key_b = {
    "name": "key for door b",
    "type": "key",
    "target": door_b,
}

key_c = {
    "name": "key for door c",
    "type": "key",
    "target": door_c,
}

key_d = {
    "name": "key for door d",
    "type": "key",
    "target": door_d,
}

key_e = {
    "name": "key for door e",
    "type": "key",
    "target": door_e,
}

game_room = {
    "name": "game room",
    "type": "room",
}

bedroom_1 = {
    "name": "bedroom 1",
    "type": "room",
}

bedroom_2 = {
    "name": "bedroom 2",
    "type": "room",
}

living_room = {
    "name": "living room",
    "type": "room",
}

entrance_hall = {
    "name": "entrance hall",
    "type": "room",
}

outside = {
    "name": "outside"
}

all_rooms = [game_room, bedroom_1, bedroom_2, living_room, outside, entrance_hall]

all_doors = [door_a, door_b, door_c, door_d, door_e]

# define which items/rooms are related


object_relations = {
    "game room": [couch, piano, door_a],
    "bedroom 1": [queen_bed, door_a, door_b, door_c],
    "bedroom 2": [double_bed, dresser, door_b],
    "living room": [dining_table, door_c, door_d],
    "entrance hall": [door_d, door_e],
    "piano": [key_a],
    "double bed": [key_c],
    "door a": [game_room, bedroom_1],
    "door b": [bedroom_1, bedroom_2],
    "door c": [bedroom_1, living_room],
    "door d": [living_room, entrance_hall],
    "door e": [entrance_hall, outside]

}

# defines the position of each human/animal
living_being = {
    "game room": [spider, gamer_guy],
    "bedroom 1": [cowboy_texas],
    "bedroom 2": [kid_2],
    "living room": [buffon_1],
    "entrance hall": [house_owner]
}

# define game state. Do not directly change this dict.
# Instead, when a new game starts, make a copy of this
# dict and use the copy to store gameplay state. This
# way you can replay the game multiple times.

INIT_GAME_STATE = {
    "current_room": game_room,
    "keys_collected": [],
    "target_room": outside
}



def linebreak():
    """
    Print a line break
    """
    print("\n\n")


def start_game():
    """
    Start the game
    """
    print(
        "You wake up on a couch and find yourself in a strange house with no windows which you have never been to before.\nYou don't remember why you are here and what had happened before.\nYou feel some unknown danger is approaching and you must get out of the house, NOW!")
    play_room(game_state["current_room"])


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
### RIDDLES ###
def coin_toss():
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
        return key_e

    else:
        print("Sadly, You guessed wrong!\n")

#----------------------------------------------------------

def bullet_position():
    bullet_position = random.randrange(1, 6, 1)
    return bullet_position

def spin_chamber():
    chamber_position = random.randrange(1, 6, 1)
    return chamber_position

def fire_gun():
    rounds = 1
    print("I have a gun with 6 chambers and 1 bullet, lets try it on your head")
    if rounds < 2:
        if bullet_position() == spin_chamber():
            return "dead"
        else:
            print("Luckily, you got yourself a key b")
            return key_b
#----------------------------------------------------------

def jogo():
    goal_keeper = ['left','middle','right']
    player=[]
    action=''

    while action not in goal_keeper and action!='panenka':
        action=input('Wild Legendary Buffon appears, you need to score a penalty to pass by him. Where do you shoot, left, middle or right? ')
        if action not in goal_keeper and action!='panenka':
            print('AIM AT THE NET')
    gr_action=random.choice(goal_keeper)
    player.append(action)

    if player[0]=='panenka':
        print('Buffon dropped a key d while running away!')
        return key_d
    else:
        if gr_action==player[0]:
            print('Buffon got lucky! Try again')
        else:
            print('GOAL!!!\nTime to celebrate\nLook Buffon is running away!\nYou see him dropping a key d!\nWe should carry our journey')
            return key_d

### RIDDLES END###

def explore_room(room):
    """
    Explore a room. List all items belonging to this room.
    """
    items = [i["name"] for i in object_relations[room["name"]]]
    lives = [i["name"] for i in living_being[room["name"]]]
    print("\nYou explore the room. This is " + room["name"], "\nYou find:\n",", ".join(lives),"\n",", ".join(items))


def get_next_room_of_door(door, current_room):
    """
    From object_relations, find the two rooms connected to the given door.
    Return the room that is not the current_room.
    """
    connected_rooms = object_relations[door["name"]]
    for room in connected_rooms:
        if (not current_room == room):
            return room


def talk_to(someone):
    """
        Talk to a living being which can be an human or animal.
        First make sure the intended living being belongs to the current room.
        Then check if the human or animal is a door or furniture. Tell player "Why are you speaking to objects?
     """
    current_room = game_state["current_room"]
    output = None

    for item in object_relations[current_room["name"]]:
        if (item["name"] == someone):
            output = "You stare at " + someone + ". After 1 hour staring you see it's lifeless "
            print(output)
            play_room(current_room)
    for live in living_being[current_room["name"]]:
        if live["name"] == someone:
            output = "You say Hi to " + someone + ". "
            print(output)
            if live["riddle"] == "flip coin":
                print(someone + " says:" + " I have something for you")
                success = coin_toss()
                if success == key_e:
                    game_state["keys_collected"].append(key_e)
                    play_room(current_room)
                else:
                    play_room(current_room)
            elif live["riddle"] == "gun fire":
                print(someone + " says:" + " I have something for you")
                success_1 = fire_gun()
                if success_1 == key_b:
                    game_state["keys_collected"].append(key_b)
                    play_room(current_room)
                elif success_1 == "dead":
                    print("\nGame Over")
                    play_room(game_room)
            elif live["riddle"] == "penalty":
                print(someone + " says:" + " I have something for you")
                success_2 = jogo()
                if success_2 == key_d:
                    game_state["keys_collected"].append(key_d)
                    play_room(current_room)
                else:
                    play_room(current_room)

            elif live["riddle"] == "none":
                output = someone +" says:" + " I have no riddles for you"
                print(output)
                play_room(current_room)
            break

    if (output is None):
        print("The one you requested is not found in the current room.")
        play_room(current_room)


def examine_item(item_name):
    """
    Examine an item which can be a door or furniture.
    First make sure the intended item belongs to the current room.
    Then check if the item is a door. Tell player if key hasn't been
    collected yet. Otherwise ask player if they want to go to the next
    room. If the item is not a door, then check if it contains keys.
    Collect the key if found and update the game state. At the end,
    play either the current or the next room depending on the game state
    to keep playing.
    """
    current_room = game_state["current_room"]
    next_room = ""
    output = None
    for live in living_being[current_room["name"]]:
        if (live["name"] == item_name):
            output = "You stare at " + item_name + ". Nothing happens..."
            print(output)

    for item in object_relations[current_room["name"]]:
        if (item["name"] == item_name):
            output = "You examine " + item_name + ". "
            if (item["type"] == "door"):
                have_key = False
                for key in game_state["keys_collected"]:
                    if (key["target"] == item):
                        have_key = True
                if (have_key):
                    output += "You unlock it with a key you have."
                    next_room = get_next_room_of_door(item, current_room)
                else:
                    output += "It is locked but you don't have the key."
            else:
                if (item["name"] in object_relations and len(object_relations[item["name"]]) > 0):
                    item_found = object_relations[item["name"]].pop()
                    game_state["keys_collected"].append(item_found)
                    output += "You find " + item_found["name"] + "."
                else:
                    output += "There isn't anything interesting about it."
            print(output)
            break

    if (output is None):
        print("The item you requested is not found in the current room.")

    if (next_room and input("Do you want to go to the next room? Enter 'yes' or 'no'").strip() == 'yes'):
        play_room(next_room)
    else:
        play_room(current_room)


game_state = INIT_GAME_STATE.copy()

start_game()

