from collections import deque

with open ("day_16_input.txt") as input_file:
    puzzle = [list(i) for i in input_file.read().split("\n")]

print(puzzle)
row_length, col_length = len(puzzle), len(puzzle[0])
print(f"(num_rows, num_cols): {row_length, col_length}")

start = [(0,-1,0,1)]
seen = set()
q = deque(start)
print(f"Seen tiles: {seen}")
print(f"Queue: {q}")

while q:
    i, j, di, dj = q.popleft()
    i += di
    j += dj
    print(f"Current position and direction: {i, j, di, dj}")
    # If in bounds of puzzle
    if i < 0 or i >= row_length or j < 0 or j >= col_length:
        continue
    char = puzzle[i][j]
    print(f"Next char {char}")
    # If '.' or splitter is in the same direction, then carry on with the same direction
    if char == "." or (char == '-' and dj != 0) or (char == '|' and di != 0):
        print("Carry on in same direction rule")
        if (i, j, di, dj) not in seen:
            seen.add((i, j, di, dj))
            q.append((i, j, di, dj))
            print(f"Seen tiles: {seen}")
            print(f"Queue: {q}")
    # If mirror '/' di, dj = -dj, -di
    elif char == "/":
        print("Mirror rule /")
        di, dj = -dj, -di
        if (i, j, di, dj) not in seen:
            seen.add((i, j, di, dj))
            q.append((i, j, di, dj))
            print(f"Seen tiles: {seen}")
            print(f"Queue: {q}")
    # If mirror '\\' di, dj = dj, di
    elif char == "\\":
        print("Mirror rule \\")
        di, dj = dj, di
        if (i, j, di, dj) not in seen:
            seen.add((i, j, di, dj))
            q.append((i, j, di, dj))
            print(f"Seen tiles: {seen}")
            print(f"Queue: {q}")
    # If splitter
    else:
        # If splitter '|', then direction is (1,0) or (-1,0)
        if char == '|':
            print("Splitter rule |")
            for di, dj in [(1, 0), (-1, 0)]:
                print(i, j, di, dj)
                if (i, j, di, dj) not in seen:
                    seen.add((i, j, di, dj))
                    q.append((i, j, di, dj))
                    print(f"Seen tiles: {seen}")
                    print(f"Queue: {q}")
        # If splitter '-', then direction is (0,1) or (0,-1)
        else:
            print("Splitter rule -")
            for di, dj in [(0, 1), (0, -1)]:
                if (i, j, di, dj) not in seen:
                    seen.add((i, j, di, dj))
                    q.append((i, j, di, dj))
                    print(f"Seen tiles: {seen}")
                    print(f"Queue: {q}")

# Remove directions to obtain unique coor.
coor = [(i[0], i[1]) for i in seen]
print(f"Length of coor list: {len(coor)}")
unique_coor = set(coor)
print(f"Length of unique coor list: {len(unique_coor)}")


