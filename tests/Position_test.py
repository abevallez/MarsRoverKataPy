import pytest

from src.Position import Position
from src.World import World

world: World = World()
default_position = Position(0, 0, 'N', world)


def test_position_is_created_with_world():
    assert isinstance(default_position.world, World)


def test_check_x_start_edge():
    assert default_position._is_start_x_edge()


def test_check_no_x_start_edge():
    position = Position(5, 0, 'N', world)
    assert position._is_start_x_edge() is False


def test_check_x_end_edge():
    position = Position(world.size_x - 1, 0, 'N', world)
    assert position._is_start_x_edge() is False


def test_check_y_start_edge():
    assert default_position._is_start_y_edge()


def test_check_no_y_start_edge():
    position = Position(0, 5, 'N', world)
    assert position._is_start_y_edge() is False


def test_check_y_end_edge():
    position = Position(0, world.size_y - 1, 'N', world)
    assert position._is_start_y_edge() is False


@pytest.mark.parametrize("direction", ['N', 'E', 'S', 'W'])
def test_is_facing_any_direction(direction):
    position = Position(0, 0, direction, world)
    assert position.is_facing(direction) is True


def test_move_forward_in_x():
    new_position: Position = default_position.move_forward()
    assert new_position.coordinates[0] == default_position.coordinates[0] + 1


def test_move_forward_in_x_in_end_edge_should_be_0():
    position: Position = Position(world.size_x - 1, 0, 'N', world)
    new_position = position.move_forward()
    assert new_position.coordinates[0] == 0


def test_move_forward_in_y():
    position: Position = Position(0, 0, 'E', world)
    new_position = position.move_forward()
    assert new_position.coordinates[1] == default_position.coordinates[1] + 1


def test_move_forward_in_y_in_end_edge_should_be_0():
    position: Position = Position(0, world.size_y - 1, 'E', world)
    new_position = position.move_forward()
    assert new_position.coordinates[1] == 0


def test_move_back_in_x():
    position: Position = Position(world.size_x - 1, 0, 'N', world)
    new_position: Position = position.move_back()
    assert new_position.coordinates[0] == position.coordinates[0] - 1


def test_move_back_in_x_in_start_edge():
    new_position = default_position.move_back()
    assert new_position.coordinates[0] == world.size_x - 1


def test_move_back_in_y():
    position: Position = Position(0, world.size_y - 1, 'E', world)
    new_position: Position = position.move_back()
    assert new_position.coordinates[1] == position.coordinates[1] - 1


def test_move_back_in_y_in_start_edge():
    position: Position = Position(0, 0, 'E', world)
    new_position: Position = position.move_back()
    assert new_position.coordinates[1] == world.size_y - 1

