# Text-Based Adventure Game

## Author Information
YourName (YourLogin)

## Repository
[Github Repository](Github/url)

## How to run the program
1. Install Python 3 if not already installed.
2. Download or clone the repository.
3. Place the game map JSON file in the same directory as the game.
4. Open a terminal or command prompt.
5. Navigate to the directory containing the game files.
6. Run the command `python3 adventure.py [map filename]` (Replace `[map filename]` with the name of your game map JSON file)

## About the program
This program is a text-based adventure game where players can explore rooms, pick up items, and interact with objects in a virtual world. The game is designed to be easily extensible with the addition of new verbs, items, and interactions. The game engine reads a JSON file to load the game world. Several verbs which can be used as commands in the game are:

1. **go**: The 'go' verb is used to navigate between rooms in the game. To use the verb, type `go [direction]`, where `[direction]` is a valid exit direction for the current room (e.g., `go north`).

2. **look**: The 'look' verb allows the player to inspect the current room, providing a description, available items, and possible exits. To use the verb, simply type `look`.

3. **get**: The 'get' verb is used to pick up items present in the current room and add them to the player's inventory. To use the verb, type `get [item]`, where `[item]` is the name of the item you want to pick up (e.g., `get rose`).

4. **drop**: The 'drop' verb allows the player to remove items from their inventory and place them in the current room. To use the verb, type `drop [item]`, where `[item]` is the name of the item you want to drop (e.g., `drop rose`).

5. **inventory**: The 'inventory' verb lists the items currently in the player's inventory. To use the verb, simply type `inventory`.

6. **help**: The 'help' verb displays a dynamically generated list of available verbs and their purposes. To use the verb, simply type `help`.

7. **quit**: The 'quit' verb ends the game and exits the program. To use the verb, simply type `quit`.

## Time spent on the project
Estimated time spent: 10 hours

## How the code was tested
The code was tested by running the game with various map files and inputs, ensuring that all implemented verbs and features work as expected. Additionally, the game was tested for edge cases and incorrect inputs to make sure it behaves correctly.

## Bugs or issues
No unresolved bugs or issues.

## Difficult issue or bug and its resolution
An issue faced during development was handling get verb with items containing spaces such as 'ancient scroll'. For this case just replaced the 'get ' with '' to clean the input and handled accordingly.

## Extensions implemented
1. **Help Verb**: A dynamic help verb that lists all available verbs, generated from the defined verbs in the code. The help verb can be accessed by typing 'help' during gameplay.
2. **Directions as Verbs**: Implemented the functionality to use exit directions as verbs, allowing players to type 'east' instead of 'go east'. As I have not implemented abbreviations so 'nw' for 'northwest' isn't implemented.
3. **Drop Verb**: Added a drop verb that allows players to remove items from their inventory and place them in the current room. The drop verb can be accessed by typing 'drop [item]'.

To exercise these extensions, simply use the respective commands during gameplay. The location of these extensions in the map depends on the map JSON file used when running the game.


## Interaction implemented
**Objects that demand custom verbs**: A **vending machine** will need the user to pull a lever and it randomly throws different items.
