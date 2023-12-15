def hash_algorithm(string):
    value = 0

    for char in string:
        value += ord(char)
        value *= 17
        value = value % 256
    return value


with open ("day_15_input.txt") as input_file:
    puzzles = [i for i in input_file.read().split(",")]
print(puzzles)

total = 0

for puzzle in puzzles:
    total += (hash_algorithm(puzzle))
    print(total)


