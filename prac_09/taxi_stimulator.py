
from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    bill = 0.0

    while True:
        print("Q)uit\nS)elect a taxi\nD)rive the selected taxi")
        choice = input(">>> ").upper()

        if choice == 'Q':
            break
        elif choice == 'S':
            print("Current available taxis are")
            for i, taxi in enumerate(taxis):
                print(f"{i} - {taxi}")
            taxi_choice = int(input("Selection: "))
            if 0 <= taxi_choice < len(taxis):
                current_taxi = taxis[taxi_choice]
            else:
                print("Invalid choice")
        elif choice == 'D':
            if current_taxi is None:
                print("Please choose a taxi ")
            else:
                distance = float(input("How many km are you driving with this car? "))
                current_taxi.start_fare()
                current_taxi.drive(distance)
                trip_cost = current_taxi.get_fare()
                print(f"Your {current_taxi.name} price is ${trip_cost:.2f}")
                bill += trip_cost
        else:
            print("Invalid option")

        print(f"Current total cost is ${bill:.2f}")

    print(f"Total cost is ${bill:.2f}")
    print("Current taxis are:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


if __name__ == "__main__":
    main()