from typing import List

position: List[int] = [0, 0]


def start(x: int = 0, y: int = 0):
    global position
    position = [x, y]


def current_position():
    return position
