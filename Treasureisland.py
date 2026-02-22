print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

con1 = input('You\'re at a cross road.' 
             'Where do you want to go?'
             'Type "Left" or "Right".\n').lower()

if con1 == "left":
    con2 = input('You\'re come to a lake.'
                 'There is an island in the middle of the lake. \n'
                 'Type "wait" to wait for a boat. '
                 'Type "swim" to swim across.\n').lower()
    if con2 == "wait":
        con3 = input('Your arrived in island unharmed. '
                     'There is house with 3 doors. \n'
                     'One "red", One "Yellow", One "Blue".\n'
                     'Which color do you want to Choose?\n').lower()
        if con3 == "red":
            print("It is a room of fire. Game Over")
        elif con3 == "yellow":
            print("You found the treasure. You win!")
        elif con3 == "blue":
            print("You ennter a room of beasts. Game Over.")
        else:
            print("You choose a door that doesn't exist. Game Over.")
    else:
        print("You got attacked by an angry trout. Game Over.")
else:
    print("You're felt into a hole. Game Over.")