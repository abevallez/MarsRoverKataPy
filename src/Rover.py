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
        if self._position.direction == 'N':
            new_position = self._move_forward_x()
        elif self._position.direction == 'E':
            new_position = self._move_forward_y()
        elif self._position.direction == 'S':
            new_position = self._move_back_x()
        elif self._position.direction == 'W':
            new_position = self._move_back_y()
        self._position = new_position

    def move_back(self):
        if self._position.direction == 'N':
            new_position = self._move_back_x()
        elif self._position.direction == 'E':
            new_position = self._move_back_y()
        elif self._position.direction == 'S':
            new_position = self._move_forward_x()
        elif self._position.direction == 'W':
            new_position = self._move_forward_y()
        self._position = new_position

    def turn_right(self):
        if self._position.direction == 'N':
            new_direction = 'E'
        elif self._position.direction == 'E':
            new_direction = 'S'
        elif self._position.direction == 'S':
            new_direction = 'W'
        elif self._position.direction == 'W':
            new_direction = 'N'
        new_position = Position(self._position.coordinates[0],
                                self._position.coordinates[1],
                                new_direction,
                                self._position.world)
        self._position = new_position

    def turn_left(self):
        if self._position.direction == 'N':
            new_direction = 'W'
        elif self._position.direction == 'W':
            new_direction = 'S'
        elif self._position.direction == 'S':
            new_direction = 'E'
        elif self._position.direction == 'E':
            new_direction = 'N'
        new_position = Position(self._position.coordinates[0],
                                self._position.coordinates[1],
                                new_direction,
                                self._position.world)
        self._position = new_position

    def current_direction(self) -> str:
        return self._position.direction

    def current_coordinates(self) -> list:
        return self._position.coordinates

    def _move_back_x(self) -> Position:
        if self._position.is_start_x_edge():
            new_x = 5
        else:
            new_x = self._position.coordinates[0] - 1

        new_position = Position(new_x,
                                self._position.coordinates[1],
                                self._position.direction,
                                self._position.world)
        return new_position

    def _move_back_y(self) -> Position:
        if self._position.is_start_y_edge():
            new_y = 5
        else:
            new_y = self._position.coordinates[1] - 1

        new_position = Position(self._position.coordinates[0],
                                new_y,
                                self._position.direction,
                                self._position.world)
        return new_position

    def _move_forward_y(self) -> Position:
        if self._position.is_end_y_edge():
            new_y = 0
        else:
            new_y = self._position.coordinates[1] + 1

        new_position = Position(self._position.coordinates[0],
                                new_y,
                                self._position.direction,
                                self._position.world)
        return new_position

    def _move_forward_x(self) -> Position:
        if self._position.is_end_x_edge():
            new_x = 0
        else:
            new_x = self._position.coordinates[0] + 1

        new_position = Position(new_x,
                                self._position.coordinates[1],
                                self._position.direction,
                                self._position.world)
        return new_position
