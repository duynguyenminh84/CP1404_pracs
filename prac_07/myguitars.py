from prac_07.guitar import Guitar


def main():

    Guitars = []
    Guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    Guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    Guitars.append(Guitar("Fender Stratocaster" ,2014,765.4))
    Guitars.append(Guitar("Martin Grand J12-16GTE",2015,2199))
    Guitars.append(Guitar("Taylor PS10ce" ,2014,9318))
    Guitars.append(Guitar("Gretsch 6120 Chet Atkins",1956,10999.99))
    print("My guitars!")

    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost:$"))
        new_guitar = Guitar(name, year, cost)
        with open("guitars.csv", "w") as f:
            f.write(name+"," + str(year)+","+str(cost))
        Guitars.append(new_guitar)
        print(new_guitar, "added")
        name = input("Name: ")

    print("These are my guitars:")
    Guitars.sort()
    for i, guitar in enumerate(Guitars, 1):

        # Note the use of the format method and numbered placeholders
        print("Guitar {0}: {1.name:>20} ({1.year}), worth ${1.cost:10,.2f}".format(i, guitar))


main()