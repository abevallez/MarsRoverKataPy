from src.World import World


class Position:

    def __init__(self, x: int, y: int, starting_direction: str, world: World):
        self._coordinates: list = [x, y]
        self._direction: str = starting_direction
        self._world: World = world

    @property
    def coordinates(self) -> list:
        return self._coordinates

    @property
    def direction(self) -> str:
        return self._direction

    @property
    def world(self) -> World:
        return self._world

    def _is_start_x_edge(self) -> bool:
        return self._coordinates[0] == 0

    def _is_end_x_edge(self) -> bool:
        return self._coordinates[0] == self._world.size_y - 1

    def _is_start_y_edge(self) -> bool:
        return self._coordinates[1] == 0

    def _is_end_y_edge(self) -> bool:
        return self._coordinates[1] == self._world.size_y - 1

    def is_facing(self, direction: str) -> bool:
        return self._direction == direction

    def _move_forward_x(self):
        if self._is_end_x_edge():
            new_x = 0
        else:
            new_x = self.coordinates[0] + 1

        new_position = Position(new_x,
                                self.coordinates[1],
                                self.direction,
                                self.world)
        return new_position

    def _move_forward_y(self):
        if self._is_end_y_edge():
            new_y = 0
        else:
            new_y = self.coordinates[1] + 1

        new_position = Position(self.coordinates[0],
                                new_y,
                                self.direction,
                                self.world)
        return new_position

    def _move_back_x(self):
        if self._is_start_x_edge():
            new_x = 5
        else:
            new_x = self.coordinates[0] - 1

        new_position = Position(new_x,
                                self.coordinates[1],
                                self.direction,
                                self.world)
        return new_position

    def _move_back_y(self):
        if self._is_start_y_edge():
            new_y = 5
        else:
            new_y = self.coordinates[1] - 1

        new_position = Position(self.coordinates[0],
                                new_y,
                                self.direction,
                                self.world)
        return new_position

    def move_forward(self):
        if self._direction == 'N':
            position = self._move_forward_x()
        elif self._direction == 'E':
            position = self._move_forward_y()
        elif self._direction == 'S':
            position = self._move_back_x()
        elif self._direction == 'W':
            position = self._move_back_y()
        return position

    def move_back(self):
        if self._direction == 'N':
            position = self._move_back_x()
        elif self._direction == 'E':
            position = self._move_back_y()
        elif self._direction == 'S':
            position = self._move_forward_x()
        elif self._direction == 'W':
            position = self._move_forward_y()
        return position

    def turn_right(self):
        if self._direction == 'N':
            new_direction = 'E'
        elif self._direction == 'E':
            new_direction = 'S'
        elif self._direction == 'S':
            new_direction = 'W'
        elif self._direction == 'W':
            new_direction = 'N'
        return Position(self._coordinates[0],
                                self._coordinates[1],
                                new_direction,
                                self._world)

    def turn_left(self):
        if self._direction == 'N':
            new_direction = 'W'
        elif self._direction == 'W':
            new_direction = 'S'
        elif self._direction == 'S':
            new_direction = 'E'
        elif self._direction == 'E':
            new_direction = 'N'
        return Position(self._coordinates[0],
                                self._coordinates[1],
                                new_direction,
                                self._world)

