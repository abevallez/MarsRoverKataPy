class Position:

    def __init__(self,
                 x: int,
                 y: int,
                 starting_direction: str):
        self._x = x
        self._y = y
        self._direction = starting_direction

    def direction(self):
        return self._direction