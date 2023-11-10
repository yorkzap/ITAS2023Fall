"""
Course: ITAS 185 - Introduction to Programming
Lab06: Vehicle Class
Description:
    This script demonstrates OOP concepts using a Vehicle class hierarchy.
    It allows users to create instances of various vehicle types, select a vehicle, and perform
    acceleration or braking operations on it.
"""

from Vehicle import Vehicle, Car, Transport, Pickup, SportsCar

def main():
    """Main function that creates vehicle instances and prompts user interaction."""
    vehicles = [
        Vehicle("Grey", "Ford", 0, 300, 2021),
        Car("Red", "Hyundai", 0, 100, 2013, 4, True),
        Transport("Blue", "SomeBrand", 0, 160, 1999, 300),
        Pickup("Yellow", "Honda", 0, 100, 2019, 4, False),
        SportsCar("Yellow", "Lamborghini", 0, 800, 2023, 2, False)
    ]

    for index, vehicle in enumerate(vehicles):
        print(f"{index + 1}: {vehicle}")

    choice = int(input("Choose a vehicle by number: ")) - 1
    selected_vehicle = vehicles[choice]

    test_selected_vehicle(selected_vehicle)

def test_selected_vehicle(vehicle):
    """Tests the selected vehicle by accelerating or applying brakes as per user input."""
    print(f"Selected vehicle: {vehicle}")

    action = input("Would you like to 'accelerate' or 'brake'? ").lower()
    
    if action == 'accelerate':
        print("Before acceleration:", vehicle)
        vehicle.accelerate()
        print("After acceleration:", vehicle)
    elif action == 'brake':
        amount = float(input("Enter the amount of braking: "))
        print(f"Before braking: {vehicle}")
        vehicle.brake(amount)
        print(f"After braking: {vehicle}")

if __name__ == "__main__":
    main()
