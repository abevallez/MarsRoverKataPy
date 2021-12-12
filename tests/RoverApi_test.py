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


@pytest.mark.parametrize("origin_coordinates, final_coordinates",
                         [([0, 0], [1, 0]), ([1, 2], [2, 2]), ([4, 1], [5, 1])])
def test_rover_move_forward(origin_coordinates, final_coordinates):
    rover_api = RoverApi
    rover_api.start(origin_coordinates[0], origin_coordinates[1], 'N')
    rover_api.execute_command(['F'])
    assert rover_api.current_coordinates() == final_coordinates


@pytest.mark.parametrize("origin_coordinates, final_coordinates",
                         [([2, 0], [1, 0]), ([3, 2], [2, 2]), ([4, 1], [3, 1])])
def test_rover_move_back(origin_coordinates, final_coordinates):
    rover_api = RoverApi
    rover_api.start(origin_coordinates[0], origin_coordinates[1], 'N')
    rover_api.execute_command(['B'])
    assert rover_api.current_coordinates() == final_coordinates


@pytest.mark.parametrize("commands, final_coordinates",
                         [(['F', 'B'], [0, 0]), (['F', 'F'], [2, 0]), (['F', 'F', 'B'], [1, 0])])
def test_rover_move_with_more_than_1_command(commands, final_coordinates):
    rover_api = RoverApi
    rover_api.start(0, 0, 'N')
    rover_api.execute_command(commands)
    assert rover_api.current_coordinates() == final_coordinates


@pytest.mark.parametrize("origin_coordinates, final_coordinates",
                         [([2, 0], [2, 1]), ([3, 2], [3, 3]), ([4, 1], [4, 2])])
def test_rover_move_right(origin_coordinates, final_coordinates):
    rover_api = RoverApi
    rover_api.start(origin_coordinates[0], origin_coordinates[1], 'N')
    rover_api.execute_command(['R'])
    assert rover_api.current_coordinates() == final_coordinates
