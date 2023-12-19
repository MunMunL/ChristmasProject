
with open("day_19_input.txt") as input_file:
    puzzle = [i.split("\n") for i in input_file.read().split("\n\n")]
print(puzzle)

# Workflows - split text as dictionary to use eval()
workflows_list = {}

workflows = puzzle[0]
for workflow in workflows:
    name, rest = workflow[:-1].split("{")
    rules = rest.split(",")
    print(name)
    workflows_list[name] = ([], rules.pop())
    for rule in rules:
        comparison, target = rule.split(":")
        print(comparison,target)
        key = comparison[0]
        operator = comparison[1]
        value = int(comparison[2:])
        workflows_list[name][0].append((key, operator, value, target))
        print(workflows_list[name])

def accept(item, name = 'in'):
    if name == 'R':
        return False
    if name == 'A':
        return True

    rules, default = workflows_list[name]

    for key, operator, value, target in rules:
        if eval(f"{item[key]}{operator}{value}"):
            return accept(item, target)

    return accept(item, default)

# Parts - split text as dictionary
total = 0
parts_list = []
parts = puzzle[1]

for part in parts:
    part = part.strip('{}')
    # print("The original string is ",part)

    part_dict = dict((a.strip(), int(b.strip()))
                  for a, b in (element.split('=')
                               for element in part.split(',')))

    if accept(part_dict):
        print(f"Part {part} accepted")
        total += sum(part_dict.values())

print(total)


