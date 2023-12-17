from heapq import heappush, heappop

with open("day_17_input.txt") as input_file:
    puzzle = [list(map(int, i)) for i in input_file.read().split("\n")]

print(puzzle)
row_length, col_length = len(puzzle), len(puzzle[0])

seen = set()
#queue = (heatloss, row_index, col_index, dir_row, dir_col, num_times_dir)
pq = [(0, 0, 0, 0, 0, 0)]

while pq:
    heat_loss, row_index, col_index, dir_row, dir_col, num_dir = heappop(pq)

    # If at end point, then print heatloss and break loop.
    if row_index == row_length -1 and col_index == col_length - 1:
        print(heat_loss)
        break

    # If seen, then skip
    if (row_index, col_index, dir_row, dir_col, num_dir) in seen:
        continue

    seen.add((row_index, col_index, dir_row, dir_col, num_dir))

    # If number times in that direction < 3
    if num_dir < 3 and (dir_row, dir_col) != (0, 0):
        next_row_index = row_index + dir_row
        next_col_index = col_index + dir_col
        # If in bound
        if (row_index >= 0 and next_row_index < row_length) and (col_index >= 0 and next_col_index < col_length):
            heappush(pq,
                     (heat_loss + puzzle[next_row_index][next_col_index],
                      next_row_index,
                      next_col_index,
                      dir_row,
                      dir_col,
                      num_dir + 1))


    # Else, change direction, not same direction forwards or backwards(reverse)
    for next_direction_row, next_direction_col in [(0,1), (1,0), (0,-1), (-1,0)]:
        if (next_direction_row, next_direction_col) != (dir_row, dir_col) and (next_direction_row, next_direction_col) != (-dir_row, -dir_col):
            next_row_index = row_index + next_direction_row
            next_col_index = col_index + next_direction_col
            # If in bount
            if (row_index >= 0 and next_row_index < row_length) and (col_index >= 0 and next_col_index < col_length):
                heappush(pq,
                         (heat_loss + puzzle[next_row_index][next_col_index],
                          next_row_index,
                          next_col_index,
                          next_direction_row,
                          next_direction_col,
                          1))

