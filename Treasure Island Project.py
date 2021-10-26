print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
print("Welcome to the Treasure Island. You're mission to find the treasure.")
choice1=input('You\'re at crossroad, where do you want to go? Type "left" or "right".\n').lower()
if choice1=="left":
    choice2=input('You\'re at the lake. Type "wait" for the boat to come or choose to "swim"\n').lower()
    if choice2=="wait":
        choice3=input("You arrive unharmed at an island. Choose one door of either Red, Yellow or Blue: \n").lower()
        if choice3=="red":
            print("Room of fire and you lose")
        elif choice3=="blue":
            print("Room of beasts. Game Over")
        elif choice3=="yellow":
            print("You found the treasure. YOU WIN!!!!!!!!")
        else:
            print("Choose an existing door")
    else:
        print("You got attacked by a trout. GAME OVER")
else:
    print("You fell into a hole. Game Over")
