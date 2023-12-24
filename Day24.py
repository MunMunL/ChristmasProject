from itertools import combinations


def line_points(line):
    x = line[0]
    y = line[1]
    z = line[2]
    vx = line[3]
    vy = line[4]
    vz = line[5]
    start = (x,y)
    n = 4000000000000000
    end = x + (n * vx), y + (n * vy)
    print([start, end])
    return [start, end]

def line_intersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
       return 'Lines do not intersect'

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div

    line1_x = [line1[0][0], line1[1][0]]
    line2_x = [line2[0][0], line2[1][0]]
    line1_y = [line1[0][1], line1[1][1]]
    line2_y =[line2[0][1], line2[1][1]]

    if min(line1_x) < x < max(line1_x) and min(line2_x) < x < max(line2_x) and min(line1_y) < y < max(line1_y) and min(line2_y) < y < max(line2_y):
        return x, y
    else:
        return 'Cross in past'


with open("day_24_input.txt") as input_file:
    hailstones = [tuple(map(int, i.replace("@", ",").split(","))) for i in input_file.read().split("\n")]
print(hailstones)

num_crosses = 0
min_limit = 200000000000000
max_limit = 400000000000000
num_hailstones = len(hailstones)
hailstones_combinations = list(combinations([i for i in range(num_hailstones)], 2))
print(f"Number of hailstones: {num_hailstones}\nCombinations: {hailstones_combinations}")


for combination in hailstones_combinations:
    print(combination)
    print(hailstones[combination[0]])
    print(hailstones[combination[1]])
    hailstone_a = line_points(hailstones[combination[0]])
    hailstone_a_start = hailstone_a[0]
    hailstone_a_end = hailstone_a[1]
    hailstone_b = line_points(hailstones[combination[1]])
    hailstone_b_start = hailstone_b[0]
    hailstone_b_end = hailstone_b[1]
    intersection = line_intersection((hailstone_a_start, hailstone_a_end), (hailstone_b_start, hailstone_b_end))
    print(f"Intersection: {intersection}")
    if intersection == 'Lines do not intersect' or intersection == 'Cross in past':
        num_crosses += 0
    elif (intersection[0] > min_limit and intersection[0] < max_limit and
            intersection[1] > min_limit and intersection[1] < max_limit):
        num_crosses += 1

print(num_crosses)