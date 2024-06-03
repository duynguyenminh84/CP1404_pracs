def get_valid_score(numb):

    if numb < 0 or numb > 100:
        print("Invalid score, try again")

    else:
        print("Your score is valid")


def print_result(number):
    if number < 0 or number > 100:
        print("Invalid")
    elif number >= 90:
        print("Excellent")
    elif number >= 50:
        print("Passable")
    else:
        print("Bad")


def show_stars(para):
    print('*' * para)

def main():


    menu = "(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"
    print(menu)

    score = int(input("Please enter your score: "))

    choice = input("Enter your choice: ").upper()

    while choice != "Q":
        if choice == "G":
            get_valid_score(score)
        elif choice == "P":
            print_result(score)
        elif choice == "S":
            show_stars(score)
        else:
            print("Invalid choice, try again")
        print(menu)
        choice = input("Enter your choice: ").upper()
    print("Farewell.")

main()
