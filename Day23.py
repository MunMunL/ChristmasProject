from collections import deque

with open("day_23_input.txt") as input_file:
    puzzle = [i for i in input_file.read().split("\n")]

# print(puzzle)
sr = sc = er = ec = 0

for row_index, row_value in enumerate(puzzle):
    for col_index, col_value in enumerate(row_value):
        if row_index == 0 and col_value == ".":
            sr = row_index
            sc = col_index
            print(f"Starting location is at: {(sr, sc)}")
        if row_index == len(puzzle) - 1 and col_value == ".":
            er = row_index
            ec = col_index
            print(f"End location is at: {(er, ec)}")


def dfs(row, col, end_row, end_col, visited, length):
    if row == end_row and col == end_col:
        return length

    if (row, col) in visited:
        return -1

    curr_visited = set(visited)
    curr_visited.add((row, col))

    curr = puzzle[row][col]
    # print(f"Current pos {curr} at {(row, col)}, ")

    # Possible list of directions
    if curr == "<":
        directions = [(0, -1)]
    elif curr == ">":
        directions = [(0, 1)]
    elif curr == "^":
        directions = [(-1, 0)]
    elif curr == "v":
        directions = [(1, 0)]
    else:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # For each direction
    to_visit = []
    for direction in directions:
        nr = row + direction[0]
        nc = col + direction[1]
        # If in bound, not forest # and new position, add to to_visit
        if (
            nr >= 0
            and nc >= 0
            and nr < len(puzzle)
            and nc < len(puzzle[0])
            and puzzle[nr][nc] != "#"
            and (nr, nc) not in curr_visited
        ):
            to_visit.append((nr, nc))
            # print(f"Possible new path to visit {(nr, nc)}")

    # if dead end
    if not to_visit:
        return -1

    # longest path

    return max(
        dfs(
            nr,
            nc,
            er,
            ec,
            curr_visited,
            length + 1,
        )
        for (nr, nc) in to_visit
    )

max_path_length = dfs(sr, sc, er, ec, set(), 0)
print(max_path_length)
