from src.Position import Position
from src.Rover import Rover
from src.World import World

STARTING_COORDINATES: list = [0, 0]
STARTING_DIRECTION: str = 'N'
rover: Rover


def start(x: int = STARTING_COORDINATES[0],
          y: int = STARTING_COORDINATES[1],
          starting_direction: str = STARTING_DIRECTION,
          world: World = World()):
    global rover
    position = Position(x, y, starting_direction, world)
    rover = Rover(position)


def current_coordinates() -> list:
    return rover.current_coordinates()


def current_direction() -> str:
    return rover.current_direction()


def execute_command(commands: list):
    for command in commands:
        if command == 'F':
            rover.move_forward()
        elif command == 'B':
            rover.move_back()
        elif command == 'R':
            rover.turn_right()
        elif command == 'L':
            rover.turn_left()

