# --- Day 3: Gear Ratios ---
# You and the Elf eventually reach a gondola lift station; he says the gondola lift will take you up to the water source, but this is as far as he can bring you. You go inside.
#
# It doesn't take long to find the gondolas, but there seems to be a problem: they're not moving.
#
# "Aaah!"
#
# You turn around to see a slightly-greasy Elf with a wrench and a look of surprise. "Sorry, I wasn't expecting anyone! The gondola lift isn't working right now; it'll still be a while before I can fix it." You offer to help.
#
# The engineer explains that an engine part seems to be missing from the engine, but nobody can figure out which one. If you can add up all the part numbers in the engine schematic, it should be easy to work out which part is missing.
#
# The engine schematic (your puzzle input) consists of a visual representation of the engine. There are lots of numbers and symbols you don't really understand, but apparently any number adjacent to a symbol, even diagonally, is a "part number" and should be included in your sum. (Periods (.) do not count as a symbol.)
#
# Here is an example engine schematic:
#
# 467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598..
# In this schematic, two numbers are not part numbers because they are not adjacent to a symbol: 114 (top right) and 58 (middle right). Every other number is adjacent to a symbol and so is a part number; their sum is 4361.
#
# Of course, the actual engine schematic is much larger. What is the sum of all of the part numbers in the engine schematic?
#

# Open file splitting each row
with open("day_3_input.txt", mode="r") as input_file:
    grid = input_file.read().splitlines()
    print(grid)
    coordinates = set()

# Find all symbols
for row_coor, row_value in enumerate(grid):
    for column_coor, char in enumerate(row_value):
        # If character is a digit or "." skip
        if char.isdigit() or char == ".":
            continue
        # For symbols identified; check the 8 surrounding spots for digits
        for current_row in [row_coor - 1, row_coor, row_coor + 1]:
            for current_column in [column_coor - 1, column_coor, column_coor + 1]:
                # Skip if out of bound rows and columns, or not a digit
                if (current_row < 0 or current_row >= len(grid)
                        or current_column < 0 or current_column >= len(grid[current_row])
                        or not grid[current_row][current_column].isdigit()):
                    continue
                # For digits identified; append coordinates of first digits
                while current_column > 0 and grid[current_row][current_column - 1].isdigit():
                    current_column -= 1
                coordinates.add((current_row, current_column))

print(coordinates)
# Go through digit coordinates to get connected numbers in string, convert to integer and append to numbers_list
numbers_list = []

for row_coor, column_coor in coordinates:
    numbers_str = ""
    while column_coor < len(grid[row_coor]) and grid[row_coor][column_coor].isdigit():
        numbers_str += grid[row_coor][column_coor]
        column_coor += 1
        print(numbers_str)
    numbers_list.append(int(numbers_str))

print(numbers_list)
print(sum(numbers_list))