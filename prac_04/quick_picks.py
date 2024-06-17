import random




def main():

    picks_count= int(input("Enter the number of picks: "))

    while picks_count < 1:
        print("Please enter a positive integer")
        picks_count = int(input("Enter the number of picks: "))
    for i in range(picks_count):
        picks= []
        for j in range(6):
            number = random.randint(1, 45)
            while number in picks:
                number = random.randint(1, 45)
            picks.append(number)
        picks.sort()
        print(" ".join(f"{number:10}" for number in picks))


main()


