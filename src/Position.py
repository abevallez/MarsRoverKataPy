class Position:

    def __init__(self, x: int, y: int, starting_direction: str):
        self._coordinates: list = [x, y]
        self._direction: str = starting_direction

    @property
    def coordinates(self) -> list:
        return self._coordinates

    @property
    def direction(self) -> str:
        return self._direction