import pytest
from src.Position import Position
from src.Rover import Rover


def test_rover_set_position_when_create_it():
    position: Position = Position(0, 0, 'N')
    rover: Rover = Rover(position)
    assert rover.position is position


@pytest.mark.parametrize("x,y", [(0, 0), (1, 5), (1, 1), (5, 3), (6, 3)])
def test_current_coordinate_get_coordinate_from_position(x, y):
    position: Position = Position(x, y, 'N')
    rover: Rover = Rover(position)
    assert rover.current_coordinates()== [x, y]


@pytest.mark.parametrize("direction", ['N','S','E','W'])
def test_current_direction_get_direction_from_position(direction):
    position: Position = Position(0, 0, direction)
    rover: Rover = Rover(position)
    assert rover.current_direction() == direction
