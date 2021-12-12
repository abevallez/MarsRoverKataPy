from src.Position import Position
from src.Rover import Rover

STARTING_COORDINATES: list = [0, 0]
STARTING_DIRECTION: str = 'N'
rover: Rover


def start(x: int = STARTING_COORDINATES[0], y: int = STARTING_COORDINATES[1], starting_direction: str = STARTING_DIRECTION):
    global rover
    position = Position(x, y, starting_direction)
    rover = Rover(position)


def current_coordinates() -> list:
    return rover.current_coordinates()


def current_direction() -> str:
    return rover.current_direction()


def execute_command(commands: list):
    rover.move_forward()
