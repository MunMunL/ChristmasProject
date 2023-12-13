from itertools import product


def generate_combinations(num_of_unknowns):
    """Generates and returns a list of all possible combinations with repeats based on number of '?' """
    arr = [".", "#"]
    return list(product(arr, repeat=num_of_unknowns))


def count_function(sequence):
    """Counts the contiguous group of damaged springs, number of connected '#' in sequence """
    damage_count = [i.count("#") for i in sequence.split(".") if i != ""]
    # print(f"Damage count {damage_count}")
    return damage_count

# Open file split by report and damage_report
with open("day_12_input.txt") as input_file:
    puzzle = [(i.split()[0], i.split()[1].split(",")) for i in input_file.read().split("\n")]
# print(puzzle)

total_combination = 0

# For each line in puzzle,
# find the position of '?'
# Generate the list of combinations to test based on number of '?' identified
# Replace each char '?' with possible combination sequence
# Calculate damage report for each possible combination, add 1 to total combination if its a possible arrangement
for record in puzzle:
    report = [i for i in record[0]]
    damage_report = [int(i) for i in record[1]]
    # print(f" The report is: {report} with  damage report: {damage_report}")

    unknown_pos = [index for index, char in enumerate(report) if char == "?"]
    # print(f"Positions of '?' in sequence: {unknown_pos}")

    combination_list = generate_combinations(len(unknown_pos))
    # print(f"List of possible combinations with {len(unknown_pos)} '?' is: {combination_list}")

    for combination in combination_list:
        complete_seq = ""
        i = 0
        for char in report:
            if i > len(unknown_pos):
                i = 0
            if char == "?":
                complete_seq += combination[i]
                i += 1
            else:
                complete_seq += char
        damage_count = count_function(complete_seq)
        if damage_count == damage_report:
            total_combination += 1
print(f"Sum of all arrangements: {total_combination}")
