import json
import sys
import random
import traceback

# Room class for Room attributes


class Room:
    def __init__(self, room_data):
        self.name = room_data['name']
        self.desc = room_data['desc']
        self.exits = room_data['exits']
        self.items = room_data.get('items', [])


# helper funtion
def remove_extra_spaces(string):
    # Remove leading and trailing spaces
    string = string.strip()

    # Replace multiple spaces with a single space
    string = ' '.join(string.split())

    return string


# Game class
class Game:
    # Init
    def __init__(self, map_file):
        with open(map_file) as f:
            map_data = json.load(f)
        self.rooms = [Room(room_data) for room_data in map_data]
        self.current_room = self.rooms[0]
        self.inventory = []
        self.valid_verbs = ['go ...', 'look', 'get ...',
                            'inventory', 'quit', 'help', 'drop']
        self.vending_items = ['pack of chips',
                              'chocolate bar', 'soda can', 'gum']
        self.directions = ['east', 'west', 'north', 'south',
                           'northeast', 'northwest', 'southeast', 'southwest']

    # Play funtion

    def play(self):
        self.print_details()
        while True:
#             try:  #handling the EOF and KeyboardInterrupt
#                 user_input = input("What would you like to do? ")
#             except EOFError:
#                 print("Use 'quit' to exit.")
#                 continue
#             except KeyboardInterrupt:
#                 print('^C')
#                 traceback.print_exc()
#                 sys.exit()
            user_input = input("What would you like to do? ")
            user_input = remove_extra_spaces(user_input)
            if not user_input:
                continue
            command = user_input.split()[0].lower()
            if command == "go":
                if (user_input.strip() == "go"):
                    print("Sorry, you need to 'go' somewhere.")
                    continue
                direction = user_input.split()[1].lower()
                self.go(direction)
            elif command == "look":
                self.look()
            elif command == "get":
                item = user_input.replace("get ", "")
                if (user_input.strip() == "get"):
                    print("Sorry, you need to 'get' something.")
                    continue
                self.get(item)
            elif command == "drop":
                item = user_input.split()[1].lower()
                self.drop(item)
            elif command == "inventory":
                self.inventory_list()
            elif command == "help":
                self.help()
            elif command == "quit":
                self.quit_game()
            else:
                for dir in self.directions:  # Implementing the direction verb extension
                    if command == dir:
                        self.go(dir)
                        break
                else:
                    print("I don't understand what you mean. Try again.")

    # printing room details
    def print_details(self):
        print("> " + self.current_room.name)
        print()
        print(self.current_room.desc)
        if not self.current_room.items:
            print()
        else:
            print()
            print("Items:", ", ".join(self.current_room.items))
            print()
        self.print_exits()
        print()

    # Printing exits

    def print_exits(self):
        exits = self.current_room.exits.keys()
        print("Exits:", " ".join(exits))

    def go(self, direction):
        if direction in self.current_room.exits:
            room_id = self.current_room.exits[direction]
            self.current_room = self.rooms[room_id]
            print("You go " + direction + ".\n")
            self.print_details()
        else:
            print("There's no way to go " + direction + ".")

    def look(self):
        self.print_details()

    def get(self, item):
        if item == "vending":  # implementing the interaction
            print("You approached the vending machine. It seems to be working, but you need to pull the lever to get stuff.")
            print("What would you like to do? 'pull/quit")
            while True:  # Main game loop
                user_input = input("> ")
                if not user_input:
                    continue
                command = user_input.split()[0].lower()
                if command == "pull":
                    item_index = random.randint(0, len(self.vending_items) - 1)
                    item_picked = self.vending_items[item_index]
                    print(
                        f"You pull the lever and a {item_picked} falls out. You pick it up and put it in your inventory.")
                    self.inventory.append(item_picked)
                    break
                elif command == "quit":
                    self.quit_game()
                else:
                    print("I don't understand what you mean. Try again.")
        else:
            if item in self.current_room.items:
                self.current_room.items.remove(item)
                self.inventory.append(item)
                print("You pick up the " + item + ".")
            else:
                print("There's no " + item + " anywhere.")

    def drop(self, item):  # Implementing the drop extension
        if item in self.inventory:
            self.inventory.remove(item)
            self.current_room.items.append(item)
            print("You drop the " + item + ".")
        else:
            print("You're not carrying a " + item + ".")

    def inventory_list(self):
        if self.inventory:
            print("Inventory:")
            for item in self.inventory:
                print("  " + item)
        else:
            print("You're not carrying anything.")

    def help(self):  # Implementing the help extension
        print("You can run the following commands: ")
        print("\n".join(self.valid_verbs))

    def quit_game(self):
        print("Goodbye!")
        sys.exit()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 adventure.py [map filename]")
        sys.exit()

    game = Game(sys.argv[1])
    game.play()
