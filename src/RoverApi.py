from typing import List

STARTING_COORDINATES: List[int] = [0, 0]
STARTING_DIRECTION = 'N'
coordinates: List[int] = [0, 0]


def start(x: int = STARTING_COORDINATES[0], y: int = STARTING_COORDINATES[1]):
    global coordinates
    coordinates = [x, y]


def current_position():
    return coordinates


def current_direction():
    return STARTING_DIRECTION