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

import numpy as np
with open("day_3_input.txt", mode="r") as input_file:
    grid = np.array([list(line) for line in input_file.read().strip().split("\n")])
    print(grid)

# print(grid[0][1])
# print(len(grid[0]))
# print(len(grid))
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
dots = ["."]
non_symbols = numbers + dots
symbols_list = []
numbers_list = []
numbers_coor_list = []

def symbols_pos():
    y = 0
    x = 0
    for y in range(len(grid)):
        while x < len(grid[0]):
            for char in grid[y][x]:
                if char not in non_symbols:
                    print(char)
                    print(y,x)
                    symbols_list.append((y, x))
                x += 1
        y += 1
        x= 0

    print(symbols_list)
    return(symbols_list)



y = 0
x = 0
for y in range(len(grid)):
    while x < len(grid[0]):
        for char in grid[y][x]:
            if char in numbers:
                print(char)
                print(y, x)
                numbers_list.append(char)
                numbers_coor_list.append((y,x))
            if grid[y][x+1] in numbers:
                x += 1
    y += 1
    x = 0

print(numbers_list)
print(numbers_coor_list)