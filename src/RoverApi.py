from src.Position import Position

STARTING_COORDINATES: list = [0, 0]
STARTING_DIRECTION: str = 'N'
position: Position


def start(x: int = STARTING_COORDINATES[0], y: int = STARTING_COORDINATES[1], starting_direction: str = STARTING_DIRECTION):
    global position
    position = Position(x, y, starting_direction)


def current_position():
    return [position._x, position._y]


def current_direction():
    return position._direction