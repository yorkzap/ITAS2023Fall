"""
    Course: ITAS 185 - Introduction to Programming
    Assigment 03: RaceTrack.py class
    Description: Visualize racetrack competitions with textual representation and champion detection.
"""

class RaceTrack:
    def __init__(self, name="ITAS Motor Speedway", length=20):
        self.__name = name
        self.__length = length

    def get_name(self):
        return self.__name

    def get_length(self):
        return self.__length

    def __str__(self, current_round, race_vehicles):
        ground_lanes = f"{self.get_name()}\nRace round[{current_round}]\n\n"

        # Generate header with lane numbers
        lane_numbers = " | ".join(map(str, range(1, len(race_vehicles) + 1)))
        ground_lanes += f"| {lane_numbers} |\n"

        # Generate race track grid
        for row in range(1, self.get_length() + 2):  # Start at 1, go one past the length
            ground_lanes += "|"
            for vehicle in race_vehicles:
                icon = vehicle.get_icon() if vehicle.get_position_int() == row - 1 else " "
                ground_lanes += f" {icon} |"
            ground_lanes += f" Position: [{row - 1}]\n"  # row - 1 to match vehicle positions

        return ground_lanes

    def champion(self, winner):
        print(f"Congratulations to the champion!\n{winner}")
