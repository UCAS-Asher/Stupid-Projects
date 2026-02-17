#Lithuianian Roulete


print("This a like Rushian Roulete, you must avoid the enemy shooting you with the shot.")

def game():
    pass

def scores():
    pass


def main():
    print("Lithuianian Roulete\n 1. Play Game\n 2.Check Scores\n 3. Exit")

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