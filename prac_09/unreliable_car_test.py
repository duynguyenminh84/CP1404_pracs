
from unreliable_car import UnreliableCar


def main():

    car = UnreliableCar("Car", 100, 50)
    for i in range(5):
        success = car.drive(1)
        if success:
            print(f"Car {i + 1}: Reliable")
        else:
            print(f"Car {i + 1}: Unreliable")


if __name__ == "__main__":
    main()