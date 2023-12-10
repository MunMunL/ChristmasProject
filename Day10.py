def direction(row, column, direction):
    # F = (row, column + 1), (row + 1, column)
    # | = (row - 1, column), (row + 1, column)
    # L = (row - 1, column), (row, column + 1)
    # - = (row, column -1), (row, column + 1)
    # J = (row, column - 1), (row - 1, column)
    # 7 = (row, column -1), (row + 1, column)

    if direction == "F":
        return [(row, column + 1), (row + 1, column)]
    elif direction == "|":
        return[(row - 1, column), (row + 1, column)]
    elif direction == "L":
        return [(row - 1, column), (row, column + 1)]
    elif direction == "-":
        return [(row, column -1), (row, column + 1)]
    elif direction == "J":
        return [(row, column - 1), (row - 1, column)]
    elif direction == "7":
        return [(row, column -1), (row + 1, column)]


# next_position = direction(1,3,"7")
# print(next_position)
# print(next_position[0])
# print(next_position[0][1])


def locate_s(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "S":
                return (i,j)

def surrounding_positions(row,column):
    surrounding_elements = [(row - 1, column - 1), (row - 1, column), (row - 1, column + 1),
                            (row,column - 1), (row, column + 1),
                            (row + 1, column -1), (row + 1, column), (row + 1, column + 1)]
    return surrounding_elements

# Open file in a grid that mirrors (rows,columns)
with open("day_10_input.txt") as input_file:
    puzzle = [list(i) for i in input_file.read().split("\n")]
    print(puzzle)

# Find position of "S"
start_position = locate_s(puzzle)
print(f"S is at: {start_position}")

surrounding_positions_list = [(1,2)]
# surrounding_positions_list = surrounding_positions(start_position[0], start_position[1])
print(f"List of surrounding positions around S to explore: {surrounding_positions_list}")

at_end = False
path = [start_position]
print(f"Path {path}")
current_position = (0,0)
all_steps = []

for position in surrounding_positions_list:
    current_position = position
    puzzle_direction = puzzle[current_position[0]][current_position[1]]
    path.append(current_position)
    print(f"Current position: {current_position}")
    print(f"Puzzle direction: {puzzle_direction}")
    print(f"Path before {path}")
    while path[-1] != path[0]:
        # If there is a direction at current position
        if puzzle[current_position[0]][current_position[1]] != ".":
            current_position_options = direction(current_position[0], current_position[1], puzzle_direction)
            print(f"Next position options: {current_position_options}")
            print(f"Option1: {current_position_options[0]}")
            print(f"Option2: {current_position_options[1]}")
            print(f"Path's last pos : {path[-1]}")
            if current_position_options[0] in path and current_position_options[1] in path:
                steps = len(path) // 2
                print(f"Steps: {steps}")
                all_steps.append(steps)
                break
            elif current_position_options[0] in path:
                print("option1")
                path.append(current_position_options[1])
                # current_position = next_position_options[1]
            elif current_position_options[1] in path:
                print("option2")
                path.append(current_position_options[0])
                # current_position = next_position_options[0]
            current_position = path[-1]
            puzzle_direction = puzzle[current_position[0]][current_position[1]]
            print(f"Path after with new coor added: {path}")
            print(f"New current coor: {current_position}")
            print(f"New current coor directiom: {puzzle_direction}")

        # If is . , no direction
        else:
            continue

        print(all_steps)

