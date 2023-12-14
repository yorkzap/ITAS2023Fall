"""
    Course: ITAS 185 - Introduction to Programming
    Assigment 03: Main program
    Description: XXXXXXXXX
"""

# Ensure the classes directory is correctly referenced for the imports
from classes.Motorcycle import Motorcycle
from classes.Truck import Truck
from classes.Tesla import Tesla
from classes.RaceTrack import RaceTrack
import os
import time

def clear_screen():
    # Clear the console screen.
    os.system('cls' if os.name == 'nt' else 'clear')

def create_vehicle_from_line(line):
    parts = line.strip().split(',')
    if parts[0] == 'Motorcycle':
        return Motorcycle(parts[1], parts[2])
    elif parts[0] == 'Truck':
        return Truck(parts[1], parts[2], parts[3].strip() == 'True')
    elif parts[0] == 'Tesla':
        return Tesla(parts[1], parts[2], parts[3].strip() == 'True')
    else:
        raise ValueError(f"Unknown vehicle type: {parts[0]}")

def main():
    race_track = RaceTrack()
    race_vehicles = []

    filename = input("Enter the filename of the vehicle data or 'exit' to quit: ")
    if filename.lower() == 'exit':
        return
    filepath = os.path.join('data', filename)
    if not os.path.isfile(filepath):
        print("File not found. Please try again.")
        return

    with open(filepath, 'r') as file:
        for line in file:
            if line.strip():  # Ignore empty lines
                vehicle = create_vehicle_from_line(line)
                race_vehicles.append(vehicle)

    current_round = 1
    race_over = False
    while not race_over:
        clear_screen()  # Clear the screen before printing the new race state
        print(race_track.__str__(current_round, race_vehicles))  # Print the updated race track

        for vehicle in race_vehicles:
            vehicle.accelerate()
            vehicle.move()
            if vehicle.get_position_int() >= race_track.get_length():
                race_track.champion(vehicle)
                race_over = True
                break

        current_round += 1
        time.sleep(0.5)  # Pause for a short time interval to watch the race progress

        if race_over:
            print("Race over!")
            break

if __name__ == "__main__":
    main()
