from typing import List

STARTING_COORDINATES: List[int] = [0, 0]
STARTING_DIRECTION: str = 'N'
coordinates: List[int]
direction: str


def start(x: int = STARTING_COORDINATES[0], y: int = STARTING_COORDINATES[1], starting_direction: str = STARTING_DIRECTION):
    global coordinates
    global direction
    coordinates = [x, y]
    direction = starting_direction


def current_position():
    return coordinates


def current_direction():
    return direction