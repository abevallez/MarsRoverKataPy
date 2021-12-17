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

    def is_start_x_edge(self) -> bool:
        return self._coordinates[0] == 0

    def is_end_x_edge(self) -> bool:
        return self._coordinates[0] == self._world.size_y - 1

    def is_start_y_edge(self) -> bool:
        return self._coordinates[1] == 0

    def is_end_y_edge(self) -> bool:
        return self._coordinates[1] == self._world.size_y - 1

    def is_facing(self, direction: str) -> bool:
        return self._direction == direction

