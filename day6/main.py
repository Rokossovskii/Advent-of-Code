import os
import numpy as np
from typing import List

turn_map = {"^": ">", ">": "v", "v": "<", "<": "^"}


def __convert_data_to_numpy_array(data):
    return np.array([list(line) for line in data.split("\n")])


def find_position_of_guards(data):
    return np.where((data == "^") | (data == "v") | (data == "<") | (data == ">"))


def turn_guard_to_right(data, coordinates):
    x, y = coordinates
    x, y = x[0], y[0]
    data[x][y] = turn_map.get(data[x][y])
    return data


def __get_position_of_opstacle_in_front_of_guard(
    direction_from_guard_position: np.ndarray,
):
    opstacle = "#"
    try:
        distance = direction_from_guard_position.tolist().index(opstacle)
    except ValueError:
        distance = -1
    print(direction_from_guard_position, distance)
        
    return distance


def move_guard_forward(data, coordinates):
    x, y  = coordinates
    x, y = x[0], y[0]
    direction_from_guard_position = []
    print(data[x][y], x, y)
    match data[x][y]:
        case "^":
            direction_from_guard_position = data[:x+1, y]
        case ">":
            direction_from_guard_position = data[x, y:]
        case "v":
            direction_from_guard_position = data[x:, y]
        case "<":
            direction_from_guard_position = data[x, :y+1]
    __get_position_of_opstacle_in_front_of_guard(direction_from_guard_position)


def is_guard_on_map(data):
    return len(find_position_of_guards(data)[0]) > 0


def solution1(data):
    data = __convert_data_to_numpy_array(data)
    print(data)
    
    move_guard_forward(data, find_position_of_guards(data))
    turn_guard_to_right(data, find_position_of_guards(data))
    move_guard_forward(data, find_position_of_guards(data))
    turn_guard_to_right(data, find_position_of_guards(data))
    move_guard_forward(data, find_position_of_guards(data))
    turn_guard_to_right(data, find_position_of_guards(data))
    move_guard_forward(data, find_position_of_guards(data))
    turn_guard_to_right(data, find_position_of_guards(data))
    


def main():
    files = os.listdir(os.path.dirname(__file__))
    solutions_data = []
    for file in files:
        if file.endswith(".aoc"):
            data = open(os.path.join(os.path.dirname(__file__), file)).read()
            solutions_data += "task1_" + file, solution1(data)
            # solutions_data += "task2_" + file, solution2(data)

    return solutions_data


if __name__ == "__main__":
    print(main())
