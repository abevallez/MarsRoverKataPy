from src.Position import Position


class Rover:
    def __init__(self, position: Position):
        self._position: Position = position

    @property
    def position(self) -> Position:
        return self._position

    def move_forward(self):
        new_position = Position(self._position.coordinates[0] + 1,
                                self._position.coordinates[1],
                                self._position.direction)
        self._position = new_position

    def move_back(self):
        new_position = Position(self._position.coordinates[0] - 1,
                                self._position.coordinates[1],
                                self._position.direction)
        self._position = new_position

    def turn_right(self):
        new_position = Position(self._position.coordinates[0],
                                self._position.coordinates[1],
                                'E')
        self._position = new_position

    def turn_left(self):
        new_position = Position(self._position.coordinates[0],
                                self._position.coordinates[1],
                                'W')
        self._position = new_position

    def current_direction(self) -> str:
        return self._position.direction

    def current_coordinates(self) -> list:
        return self._position.coordinates
