#Lithuianian Roulete

import random


print("This a like Rushian Roulete, you must avoid the enemy shooting you with the shot.")

def game_loop(lives, enemy_lives, gun):
    print(f"Your Turn\nLives:{lives}\nEnemy Lives:{enemy_lives}")
    choice = input("Shoot(Y/N): ")

    if choice == "Y" or choice == "y":
        if gun[0] == "S":
            print("The gun clicked... A loud boom was heard... Ehh sorry...")
            enemy_lives -= 1
            if enemy_lives < 1:
                print("You won... Ehh nepala...")
                return
            gun = random.sample(["B","B","B","B","B","S"], 6)
        else:
            gun.remove(gun[0])
            print("The gun clicked... It was empty")
    elif choice == "N" or choice == "n":
        print("You forfeit the gun... You hope it doesnt have the shot")
    else:
        print("You didnt feel like trying... You gave up your turn")

    comp_shoot = random.choice(["Y","N"])

    if comp_shoot == "Y":
        if gun[0] == "S":
            print("The gun clicked... A loud laugh was heard... HEHEHEHA!\n")
            lives -= 1
            if lives < 1:
                print("You lost... MEGAKNIGHT!")
                return
            gun = random.sample(["B","B","B","B","B","S"], 6)
        else:
            print("The gun clicked... He didnt BM...\n")
    else:
        print("He waited planning out his next move...\n")

    game_loop(lives, enemy_lives, gun)
            

def game():
    print("Loading the gun...\nYou have 3 lives, dont die\n")
    gun = random.sample(["B","B","B","B","B","S"], 6)
    game_loop(3,3,gun)
    main()


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