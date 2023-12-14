"""
    Course: ITAS 185 - Introduction to Programming
    Assigment 03: RaceTrack.py class
    Description: XXXXXXXXX
"""

class RaceTrack:
    def __init__(self, name: str = "ITAS Motor Speedway", length: int = 20):
        self._name = name
        self._length = length

    def get_name(self) -> str:
        """Return the name of the race track."""
        return self._name

    def get_length(self) -> int:
        """Return the length of the race track."""
        return self._length

    def __str__(self, vehicles) -> str:
        """Return a string representation of the race track with vehicle positions."""
        # Header for the racetrack display
        track_representation = f"Round of the race at {self._name}:\n"

        # Initialize the track display for each position
        track_lines = ['|' for _ in range(self._length)]

        # Iterate over each vehicle to place it on the track
        for vehicle in vehicles:
            position = vehicle.get_position_int()
            # Ensure that the position does not exceed the track length
            position = min(position, self._length - 1)
            # Place the vehicle icon at its position
            track_lines[position] += vehicle.get_icon()

        # Fill the rest of the track with spaces and end with a lane marker
        for i in range(self._length):
            track_lines[i] += ' ' * (len(vehicles) - len(track_lines[i])) + '|'

        # Combine all track lines into a single string
        track_representation += '\n'.join(track_lines) + '\n'
        return track_representation

    def champion(self, winner) -> None:
        """Display the winner of the race."""
        print(f"Congratulations to the champion: {winner}")
