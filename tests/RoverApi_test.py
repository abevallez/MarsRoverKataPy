import pytest

from src import RoverApi


def test_create_rover_at_00_when_no_given_starting_point():
    rover_api = RoverApi
    rover_api.start()
    assert rover_api.current_coordinates() == [0, 0]


@pytest.mark.parametrize("x", [0, 1, 2, 4])
@pytest.mark.parametrize("y", [0, 1, 6, 7])
def test_create_rover_at_coordinates_given_as_starting_point(x, y):
    rover_api = RoverApi
    rover_api.start(1, 1)
    assert rover_api.current_coordinates() == [1, 1]


def test_create_rover_at_direction_north_when_no_direction_given():
    rover_api = RoverApi
    rover_api.start(1, 1)
    assert rover_api.current_direction() == 'N'


@pytest.mark.parametrize("direction", ['N', 'S', 'W', 'E'])
def test_create_rover_at_direction_given_as_starting_direction(direction):
    rover_api = RoverApi
    rover_api.start(0, 0, direction)
    assert rover_api.current_direction() == direction


def test_rover_move_forward():
    rover_api = RoverApi
    rover_api.start(0, 0, 'N')
    rover_api.execute_command(['F'])
    assert rover_api.current_coordinates() == [1, 0]
