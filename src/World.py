class World():
    def __init__(self, size_x: int = 6, size_y: int = 6):
        self._size_x = size_x
        self._size_y = size_y

    @property
    def size_x(self) -> int:
        return self._size_x

    @property
    def size_y(self) -> int:
        return self._size_y
