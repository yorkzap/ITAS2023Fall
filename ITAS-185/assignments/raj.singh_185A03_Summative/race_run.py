"""
    Course: ITAS 185 - Introduction to Programming
    Assigment 03: Main program
    Description: XXXXXXXXX
"""

import os
from classes.Vehicle import Vehicle
from classes.Motorcycle import Motorcycle
from classes.Truck import Truck
from classes.Tesla import Tesla
from classes.RaceTrack import RaceTrack
import random

# Helper function to parse a line from the vehicle data files
def parse_vehicle_data(line):
    parts = line.split(',')
    if parts[0] == "Motorcycle":
        return Motorcycle(parts[1], parts[2])
    elif parts[0] == "Truck":
        return Truck(parts[1], parts[2], parts[3].strip() == 'True')
    elif parts[0] == "Tesla":
        return Tesla(parts[1], parts[2], parts[3].strip() == 'True')
    else:
        raise ValueError("Unknown vehicle type")

# Main function to run the race simulation
def run_race():
    # Prompt for the vehicle data file
    while True:
        filename = input("Enter the filename of the vehicle data or 'exit' to quit: ")
        if filename.lower() == 'exit':
            return
        if os.path.exists(f"data/{filename}"):
            break
        else:
            print("File not found, please try again.")

    # Read vehicle data and create vehicle objects
    race_vehicles = []
    with open(f"data/{filename}", 'r') as file:
        for line in file:
            if line.strip():  # Skip empty lines
                vehicle = parse_vehicle_data(line)
                race_vehicles.append(vehicle)

    # Create the racetrack
    race_track = RaceTrack()

    # Run the race simulation
    round = 1
    while True:
        # Display the race track
        print(race_track.__str__(race_vehicles))

        # Check if any vehicle has won
        for vehicle in race_vehicles:
            if vehicle.get_position() >= race_track.get_length():
                race_track.champion(vehicle)
                return

        # Update the positions of the vehicles
        for vehicle in race_vehicles:
            vehicle.accelerate()
            vehicle.move()
            # Add randomness to acceleration if needed
            variance = random.choices([-0.2, -0.1, 0, 0.1, 0.2], weights=[1, 2, 6, 2, 1], k=1)[0]
            vehicle.set_speed(vehicle.get_speed() + variance)

        # Increment the round counter
        round += 1

# Run the main race simulation
if __name__ == "__main__":
    run_race()
