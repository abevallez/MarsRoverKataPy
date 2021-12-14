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
def test_rover_move_with_more_than_1_command_same_direction(commands, final_coordinates):
    rover_api = RoverApi
    rover_api.start(0, 0, 'N')
    rover_api.execute_command(commands)
    assert rover_api.current_coordinates() == final_coordinates


@pytest.mark.parametrize("origin_direction, final_direction",
                         [('N', 'E'), ('E', 'S'), ('S', 'W'), ('W', 'N')])
def test_rover_turn_direction_to_right(origin_direction, final_direction):
    rover_api = RoverApi
    rover_api.start(0, 0, origin_direction)
    rover_api.execute_command(['R'])
    assert rover_api.current_direction() == final_direction


@pytest.mark.parametrize("origin_direction, final_direction",
                         [('N', 'W'), ('W', 'S'), ('S', 'E'), ('E', 'N')])
def test_rover_turn_direction_to_left(origin_direction, final_direction):
    rover_api = RoverApi
    rover_api.start(0, 0, origin_direction)
    rover_api.execute_command(['L'])
    assert rover_api.current_direction() == final_direction


@pytest.mark.parametrize("direction, final_coordinates",
                         [('E', [2, 4]), ('W', [2, 0]), ('S', [0, 2])])
def test_rover_move_forward_when_no_facing_north(direction, final_coordinates):
    rover_api = RoverApi
    rover_api.start(2, 2, direction)
    rover_api.execute_command(list('FF'))
    assert rover_api.current_coordinates() == final_coordinates


@pytest.mark.parametrize("direction, final_coordinates",
                         [('E', [2, 0]), ('W', [2, 4]), ('S', [4, 2])])
def test_rover_move_forward_when_no_facing_north(direction, final_coordinates):
    rover_api = RoverApi
    rover_api.start(2, 2, direction)
    rover_api.execute_command(list('BB'))
    assert rover_api.current_coordinates() == final_coordinates


def test_rover_move_to_x0_when_move_toward_x_edge():
    rover_api = RoverApi
    rover_api.start(5, 0, 'N')
    rover_api.execute_command(list('F'))
    assert rover_api.current_coordinates() == [0, 0]


def test_rover_move_to_x5_when_move_back_toward_x_edge():
    rover_api = RoverApi
    rover_api.start(0, 0, 'N')
    rover_api.execute_command(list('B'))
    assert rover_api.current_coordinates() == [5, 0]


def test_rover_move_to_y0_when_move_toward_y_edge():
    rover_api = RoverApi
    rover_api.start(0, 5, 'E')
    rover_api.execute_command(list('F'))
    assert rover_api.current_coordinates() == [0, 0]


def test_rover_move_to_y5_when_move_back_toward_y_edge():
    rover_api = RoverApi
    rover_api.start(0, 0, 'E')
    rover_api.execute_command(list('B'))
    assert rover_api.current_coordinates() == [0, 5]
