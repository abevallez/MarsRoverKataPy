from src import RoverApi


def test_rover_start_at_00_when_no_given_starting_point():
    rover_api = RoverApi
    rover_api.start()
    assert rover_api.current_position() == [0, 0]


def test_rover_start_at_11_when_11_given_as_starting_point():
    rover_api = RoverApi
    rover_api.start(1, 1)
    assert rover_api.current_position() == [1,1]
