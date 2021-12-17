from src.Position import Position

NORTH = 'N'
SOUTH = 'S'
EAST = 'E'
WEST = 'W'


class Rover:

    def __init__(self, position: Position):
        self._position: Position = position

    @property
    def position(self) -> Position:
        return self._position

    def move_forward(self):
        self._position = self._position.move_forward()

    def move_back(self):
        self._position = self._position.move_back()

    def turn_right(self):
        self._position = self._position.turn_right()

    def turn_left(self):
        self._position = self._position.turn_left()

    def current_direction(self) -> str:
        return self._position.direction

    def current_coordinates(self) -> list:
        return self._position.coordinates

