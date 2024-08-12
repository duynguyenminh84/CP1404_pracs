"""
CP1404/CP5632 Practical
Test Taxi
"""
from taxi import Taxi


def main():

    my_taxi = Taxi("Prius 1", 100)
    my_taxi.drive(40)
    print(my_taxi)
    print(f"Taxi current fare is ${my_taxi.get_fare():.2f}")
    my_taxi.start_fare()
    my_taxi.drive(100)
    print(my_taxi)
    print(f"Taxi current fare is ${my_taxi.get_fare():.2f}")


if __name__ == "__main__":
    main()