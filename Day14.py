
def process_col(col_index):
    # For each col, check each row to identify blocks of #
    row_index = 0
    total = 0
    print(f"col {col_index}")

    while row_index < row_length:
        # While going through each row, identify where there are #, break into blocks
        while row_index < row_length and platform[row_index][col_index] == "#":
            row_index += 1

        count_rocks = 0
        start = row_index

        # While not #, within the block, identify num of rocks in that block
        while row_index < row_length and platform[row_index][col_index] != "#":
            if platform[row_index][col_index] == "O":
                count_rocks += 1
            row_index += 1

        print(f" Range from {start} to {row_index}, num rocks = {count_rocks}")

        # For each rock, the load is row_length - pos_of_rock
        for pos_of_rock in range(start, start + count_rocks):
            total += row_length - pos_of_rock
            print(f"Rock {pos_of_rock} with load {row_length - pos_of_rock}, running total {total}")
    return total


grand_total = 0

with open ("day_14_input.txt") as input_file:
    platform = [list(i) for i in input_file.read().split("\n")]
row_length, col_length = len(platform), len(platform[0])
print(row_length, col_length)


for col_index in range(col_length):
    grand_total += process_col(col_index)
    print(process_col(col_index))
print(grand_total)
