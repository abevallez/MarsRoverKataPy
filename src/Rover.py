from src.Position import Position


class Rover:
    def __init__(self, position: Position):
        self._position: Position = position

    @property
    def position(self) -> Position:
        return self._position

    def move_forward(self) -> Position:
        new_position = Position(self._position.coordinates[0]+1, self._position.coordinates[1], self._position.direction)
        self._position = new_position
        return self._position

    def current_coordinates(self) -> list:
        return self._position.coordinates

    def current_direction(self) -> str:
        return self._position.direction
