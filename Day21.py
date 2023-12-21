from collections import deque

with open("day_21_input.txt") as input_file:
    puzzle = [i for i in input_file.read().split("\n")]

# print(puzzle)
sr = 0
sc = 0

for row_index, row_value in enumerate(puzzle):
    for col_index, col_value in enumerate(row_value):
        if col_value == "S":
            sr = row_index
            sc = col_index
            print(f"Starting location is at: {(sr, sc)}")

plots = set()
seen = {(sr, sc)}
# q = (row, col, steps remaining)
q = deque([(sr, sc, 64)])

while q:
    row, col, steps_remaining = q.popleft()
    print(f"Current element: {row, col, steps_remaining}")

    # If even steps_remaining, possible plot
    if steps_remaining % 2 == 0:
        plots.add((row, col))
        print(f"Even num steps remaining, possible plot.")
    if steps_remaining == 0:
        continue

    for nr, nc in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]:
        print(f"Check {nr, nc}")
        # If row/col out of bounds, or rock, or in seen then skip
        if (nr < 0 or nr >= len(puzzle) or
                nc < 0 or nc >= len(puzzle[0]) or
                puzzle[nr][nc] == "#" or
                (nr, nc) in seen):
            continue
        seen.add((nr, nc))
        q.append((nr, nc, steps_remaining - 1))
        print(f"Possible plot {nr, nc}")

print(len(plots))