#Lithuianian Roulete

import random


print("This a like Rushian Roulete, you must avoid the enemy shooting you with the shot.")

def game_loop(lives, enemy_lives, gun):
    print(f"Your Turn\nLives:{lives}\nEnemy Lives:{enemy_lives}")
    choice = input("Shoot(Y/N)")

    if choice == "Y" or "y":
        if gun[0] == 1:
            

def game():
    print("Loading the gun...\nYou have 3 lives, dont die\n")
    gun = random.shuffle([0,0,0,0,0,1])
    game_loop(3,3,gun)


def scores():
    pass


def main():
    print("Lithuianian Roulete\n1. Play Game\n2.Check Scores\n3. Exit")

    choice = input("Choose a Number: ")

    if choice == "1":
        game()
    elif choice == "2":
        scores()
    elif choice == "3":
        print("Quiting...")
    else:
        print("Not an Option\n")
        main()


main()