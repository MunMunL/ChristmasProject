from itertools import product

def generate_combinations(num_of_unkowns):
    arr = [".", "#"]
    return list(product(arr, repeat=num_of_unkowns))


with open("day_12_input.txt") as input_file:
    puzzle = [(i.split()[0], i.split()[1].split(",")) for i in input_file.read().split("\n")]
print(puzzle)

for record in puzzle:
    complete_seq_list = []
    report = [i for i in record[0]]
    damage_report = [int(i) for i in record[1]]
    print(f" The report is: {report} with  damage report: {damage_report}")

    unknown_pos = [index for index, char in enumerate(report) if char == "?"]
    print(f"Positions of '?' in sequence: {unknown_pos}")

    combination_list = generate_combinations(len(unknown_pos))
    print(f"List of possible combinations with {len(unknown_pos)} '?' is: {combination_list}")

    for combination in combination_list:
        updated_report = report
        print(updated_report)
        for position in unknown_pos:
           i = 0
           while i < len((unknown_pos)):
               updated_report[i] = combination[i]
               print(updated_report)
               i += 1
           complete_seq_list.append(updated_report)


print(complete_seq_list)
print(len(complete_seq_list))


