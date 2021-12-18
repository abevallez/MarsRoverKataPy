from src.World import World


def test_world_is_created_default():
    world = World()
    assert world.size_x == 6
    assert world.size_y == 6
