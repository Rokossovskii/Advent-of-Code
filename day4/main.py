import os
import math


def insert_character_margin_on_data(data, margin=3):
    data = data.split("\n")
    length_of_column = len(data[0])
    top_margin = bottom_margin = "-" * (length_of_column + margin * 2)
    return (
        [top_margin] * margin
        + ["-" * margin + line + "-" * margin for line in data]
        + [bottom_margin] * margin
    )


def __serach_for_string_in_one_direction(data, coordinates, string, angle):
    radian = math.radians(angle)
    x_origin, y_origin = coordinates
    for i in range(len(string)):
        x, y = (
            x_origin + int(round(math.cos(radian))) * i,
            y_origin + int(round(math.sin(radian))) * i,
        )
        if data[y][x] != string[i]:
            return 0
    return 1


def search_for_string_in_all_directions(data, coordinates, string):
    x, y = coordinates
    sum_of_occurences_in_all_directions = 0
    if data[y][x] != string[0]:
        return sum_of_occurences_in_all_directions
    for angle in [0, 45, 90, 135, 180, 225, 270, 315]:
        sum_of_occurences_in_all_directions += __serach_for_string_in_one_direction(
            data, coordinates, string, angle
        )
    return sum_of_occurences_in_all_directions


def find_string_in_data(data, original_data, string):
    original_data = original_data.split("\n")
    shift = len(string) - 1
    x_len, y_len = len(original_data[0]), len(original_data)
    sum_of_occurences = 0
    for y in range(y_len):
        for x in range(x_len):
            sum_of_occurences += search_for_string_in_all_directions(
                data, (x + shift, y + shift), string
            )
    return sum_of_occurences


def solution1(data):
    word = "XMAS"
    raw_data_with_margin = insert_character_margin_on_data(data)
    return find_string_in_data(raw_data_with_margin, data, word)


def serch_for_patern_in_chunk(chunk, string="MAS"):
    number_of_occurences = 0
    for angle in [45, 135, 225, 315]:
        radian = math.radians(angle)
        coordinates = int(round(math.cos(radian))), int(round(math.sin(radian)))
        coordinates_to_search = (
            coordinates,
            (0, 0),
            (coordinates[0] * -1, coordinates[1] * -1),
        )
        test = "".join(
            [
                chunk[coordinates[1] + 1][coordinates[0] + 1]
                for coordinates in coordinates_to_search
            ]
        )
        if test == string:
            number_of_occurences += 1
    if number_of_occurences == 2:
        return 1
    return 0


def take_subchunk(data, x, y, width=3, height=3):
    return [data[y + i][x : x + width] for i in range(height)]


def solution2(data):
    data = data.split("\n")
    x_len, y_len = len(data[0]) - 2, len(data) - 2
    number_of_occurences = 0
    for y in range(y_len):
        for x in range(x_len):
            chunk = take_subchunk(data, x, y)
            number_of_occurences += serch_for_patern_in_chunk(chunk)

    return number_of_occurences


def main():
    files = os.listdir(os.path.dirname(__file__))
    solutions_data = []
    for file in files:
        if file.endswith(".aoc"):
            data = open(os.path.join(os.path.dirname(__file__), file)).read()
            solutions_data += "task1_" + file, solution1(data)
            solutions_data += "task2_" + file, solution2(data)

    return solutions_data


if __name__ == "__main__":
    # TODO Clean the code
    print(main())
