from src.Position import Position

STARTING_COORDINATES: list = [0, 0]
STARTING_DIRECTION: str = 'N'
position: Position


def start(x: int = STARTING_COORDINATES[0], y: int = STARTING_COORDINATES[1], starting_direction: str = STARTING_DIRECTION):
    global position
    position = Position(x, y, starting_direction)


def current_position() -> list:
    return position.coordinates


def current_direction() -> str:
    return position.direction