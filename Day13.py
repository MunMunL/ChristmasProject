
def mirror_line(puzzle):
    """Find the mirror line through slicing puzzle"""
    # For each row, (range starts from 1 to include 1 element in slice),
    # split puzzle to top and bottom with top half reversed to compare top == bottom
    # Trim top and bottom to have equal lengths then compare if top == bottom
    for row in range(1, len(puzzle)):
        print(f"row {row} {puzzle[row]}")
        top = (puzzle[:row][::-1])
        bottom = (puzzle[row:])
        print(top)
        print(bottom)

        top = top[:len(bottom)]
        bottom = bottom[:len(top)]

        print(top)
        print(bottom)

        if top == bottom:
            print("yes")
            return row

    print("no")
    return 0

row = 0
col = 0

with open("day_13_input.txt") as input_file:
    puzzles = [i.split("\n") for i in input_file.read().split("\n\n")]

# For each puzzle, find the mirror_line
for puzzle in puzzles:
    row += mirror_line(puzzle)

    # For column use zip to transpose grid
    col += mirror_line((list(zip(*puzzle))))
    total = col + 100 * row


print(f"Total number of rows: {row}")
print(f"Total number of cols: {col}")
print(f"Total : {total}")
