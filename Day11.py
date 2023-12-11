""""
--- Day 11: Cosmic Expansion ---
You continue following signs for "Hot Springs" and eventually come across an observatory. The Elf within turns out to be a researcher studying cosmic expansion using the giant telescope here.

He doesn't know anything about the missing machine parts; he's only visiting for this research project. However, he confirms that the hot springs are the next-closest area likely to have people; he'll even take you straight there once he's done with today's observation analysis.

Maybe you can help him with the analysis to speed things up?

The researcher has collected a bunch of data and compiled the data into a single giant image (your puzzle input). The image includes empty space (.) and galaxies (#). For example:

...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
The researcher is trying to figure out the sum of the lengths of the shortest path between every pair of galaxies. However, there's a catch: the universe expanded in the time it took the light from those galaxies to reach the observatory.

Due to something involving gravitational effects, only some space expands. In fact, the result is that any rows or columns that contain no galaxies should all actually be twice as big.

In the above example, three columns and two rows contain no galaxies:

   v  v  v
 ...#......
 .......#..
 #.........
>..........<
 ......#...
 .#........
 .........#
>..........<
 .......#..
 #...#.....
   ^  ^  ^
These rows and columns need to be twice as big; the result of cosmic expansion therefore looks like this:

....#........
.........#...
#............
.............
.............
........#....
.#...........
............#
.............
.............
.........#...
#....#.......
Equipped with this expanded universe, the shortest path between every pair of galaxies can be found. It can help to assign every galaxy a unique number:

....1........
.........2...
3............
.............
.............
........4....
.5...........
............6
.............
.............
.........7...
8....9.......
In these 9 galaxies, there are 36 pairs. Only count each pair once; order within the pair doesn't matter. For each pair, find any shortest path between the two galaxies using only steps that move up, down, left, or right exactly one . or # at a time. (The shortest path between two galaxies is allowed to pass through another galaxy.)

For example, here is one of the shortest paths between galaxies 5 and 9:

....1........
.........2...
3............
.............
.............
........4....
.5...........
.##.........6
..##.........
...##........
....##...7...
8....9.......
This path has length 9 because it takes a minimum of nine steps to get from galaxy 5 to galaxy 9 (the eight locations marked # plus the step onto galaxy 9 itself). Here are some other example shortest path lengths:

Between galaxy 1 and galaxy 7: 15
Between galaxy 3 and galaxy 6: 17
Between galaxy 8 and galaxy 9: 5
In this example, after expanding the universe, the sum of the shortest path between all 36 pairs of galaxies is 374.

Expand the universe, then find the length of the shortest path between every pair of galaxies. What is the sum of these lengths?
"""

from itertools import combinations


def rSubset(arr,r):
    """List of different combinations with no repeats from list"""
    return list(combinations(arr,r))


def locate_planets(grid):
    """For grid, identify all planets as "#" and append its (row,col) coor to planet_list"""
    for row, row_ele in enumerate(grid):
        for col, col_ele in enumerate(row_ele):
            # print((row, col), grid[row][col])
            if grid[row][col] == "#":
                planets_list.append((row, col))

num_planets = []
r=2
planets_list = []
distances_list = []

# Open file as a grid, individual char identifiable as grid[row][col]
with open("day_11_input.txt") as input_file:
    grid = [list(i) for i in input_file.read().split("\n")]

# Identify all empty rows and columns
empty_rows = [r for r, row in enumerate(grid) if all(char == "." for char in row)]
empty_cols = [c for c, col in enumerate(zip(*grid)) if all(char == "." for char in col)]
print(f"Index of empty rows: {empty_rows}")
print(f"Index of empty cols: {empty_cols}")

# Identify all planets in grid with its (row, col) coor in planet_list
locate_planets(grid)
print(f"Coor of {len(planets_list)} planets (row, col): {planets_list}")

# Create a sequenced list starting with 1 to length of planets identified -
# to create an array to find all possible planet combinations
for planet_seq in range (len(planets_list)):
    num_planets.append(planet_seq + 1)
print(f"List of located planets sequence: {num_planets}")

planet_combinations = rSubset(num_planets, r)
print(f"List of combination of planets, (planet a, planet b):\n {planet_combinations}")

# For each planet combination (a,b) identified,
# distance between planets = row distance (a,b) + col distance (a,b) + extra distance if within empty rows
for combination in planet_combinations:
    planet_a = planets_list[combination[0] - 1]
    planet_b = planets_list[combination[1] - 1]
    print(planet_a, planet_b)
    # Calculate row and col distance between planets
    distance = abs(planet_b[0] - planet_a[0]) + abs(planet_b[1] - planet_a[1])
    print(f"Distance between planets {combination} with coor: {planet_a, planet_b} is {distance}")

    # Calculate extra distance if there's any empty row/col between planets
    extra_distance = 0
    for empty_row in empty_rows:
        if min(planet_a[0], planet_b[0]) < empty_row < max(planet_a[0], planet_b[0]):
            extra_distance += 1

    for empty_col in empty_cols:
        if min(planet_a[1], planet_b[1]) < empty_col < max(planet_a[1], planet_b[1]):
            extra_distance += 1
    print(f"Extra distance to add {extra_distance}")
    total_distance = distance + extra_distance
    print(f"Total distance to add {total_distance}")
    distances_list.append(total_distance)

print(f"Sum of all lengths: {sum(distances_list)}")