
from silver_service_taxi import SilverServiceTaxi


def main():
    taxi = SilverServiceTaxi("Hummer", 200, 2)
    taxi.start_fare()
    taxi.drive(18)
    fare = taxi.get_fare()
    estimated_fare = 48.80
    assert fare == estimated_fare, f"The estimated fare is ${estimated_fare:.2f}, but got ${fare:.2f}"
    print(f"Test passed! Fare: ${fare:.2f}")


if __name__ == "__main__":
    main()