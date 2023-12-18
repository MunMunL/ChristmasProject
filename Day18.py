with open("day_18_input.txt") as input_file:
    lines = [(i.split(" ")[0], i.split(" ")[1], i.split(" ")[2]) for i in input_file.read().split("\n")]

row, col = (0,0)
seen = set()

for line in lines:
    direction, dist, color = (line[0], int(line[1]), line[2])

    if direction == 'U':
        for i in range(dist):
            row -= 1
            seen.add((row,col))
    elif direction == 'D':
        for i in range(dist):
            row += 1
            seen.add((row,col))
    elif direction == 'L':
        for i in range(dist):
            col -= 1
            seen.add((row,col))
    elif direction == 'R':
        for i in range(dist):
            col += 1
            seen.add((row,col))



sorted_seen = (sorted(seen))
print(f"List of coor seen in a sorted order: {sorted(seen)}")

first_row = (sorted_seen[0][0])
last_row = (sorted_seen[-1][0])
first_col = (min(sorted_seen[1]))
last_col = (max(sorted_seen[1]))
print(f"Row range of terrain is {first_row} to {last_row}."
      f"\nCol range of terrain is {first_col} to {last_col}.")

dug_out_list = []

for row in range(first_row, last_row + 1):
    print(f"At row {row}")

    list = []
    for coor in sorted_seen:
        # if row_index match add to list, get col min and max; amt dug = max - min + 1
        if coor[0] == row:
            print(f"For {coor} add {coor[1]} to list")
            list.append(coor[1])
    print(f"Max in list is {max(list)} and min in list is {min(list)}."
          f"\nAmount dug out in row {row} is {max(list) - min(list) + 1}")
    dug_out_list.append(max(list) - min(list) + 1)

print(dug_out_list)
print(len(dug_out_list))
print(f"Total cubic meters: {sum(dug_out_list)}")