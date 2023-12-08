# --- Day 8: Haunted Wasteland ---
# You're still riding a camel across Desert Island when you spot a sandstorm quickly approaching. When you turn to warn the Elf, she disappears before your eyes! To be fair, she had just finished warning you about ghosts a few minutes ago.
#
# One of the camel's pouches is labeled "maps" - sure enough, it's full of documents (your puzzle input) about how to navigate the desert. At least, you're pretty sure that's what they are; one of the documents contains a list of left/right instructions, and the rest of the documents seem to describe some kind of network of labeled nodes.
#
# It seems like you're meant to use the left/right instructions to navigate the network. Perhaps if you have the camel follow the same instructions, you can escape the haunted wasteland!
#
# After examining the maps for a bit, two nodes stick out: AAA and ZZZ. You feel like AAA is where you are now, and you have to follow the left/right instructions until you reach ZZZ.
#
# This format defines each node of the network individually. For example:
#
# RL
#
# AAA = (BBB, CCC)
# BBB = (DDD, EEE)
# CCC = (ZZZ, GGG)
# DDD = (DDD, DDD)
# EEE = (EEE, EEE)
# GGG = (GGG, GGG)
# ZZZ = (ZZZ, ZZZ)
# Starting with AAA, you need to look up the next element based on the next left/right instruction in your input. In this example, start with AAA and go right (R) by choosing the right element of AAA, CCC. Then, L means to choose the left element of CCC, ZZZ. By following the left/right instructions, you reach ZZZ in 2 steps.
#
# Of course, you might not find ZZZ right away. If you run out of left/right instructions, repeat the whole sequence of instructions as necessary: RL really means RLRLRLRLRLRLRLRL... and so on. For example, here is a situation that takes 6 steps to reach ZZZ:
#
# LLR
#
# AAA = (BBB, BBB)
# BBB = (AAA, ZZZ)
# ZZZ = (ZZZ, ZZZ)
# Starting at AAA, follow the left/right instructions. How many steps are required to reach ZZZ?

# Function to read network and provide as a tuple (position, left, right)
def nodes_map(location):
    for nodes in network:
        (position, left, right) = nodes
        if position == location:
            return(position, left, right)


number_iterations = 1
current_pos = "AAA"
at_end = False

# Open file to retrieve directions as a list and network mapping as a tuple (position, left, right)
with open("day_8_input.txt") as input_file:
    raw_file = input_file.read().strip().split("\n\n")
    print(raw_file)

directions = raw_file[0]
print(f"Game directions: {directions}")

network = [(i.split("=")[0].strip(),
            i.split("=")[1].strip("( ) ").split(",")[0],
            i.split("=")[1].strip("( ) ").split(",")[1].strip())
           for i in raw_file[1].split("\n")]
print(f"Network mapping: {network}")

# While loop loops the set of directions and repeats till reached ZZZ (at_end = True).
while not at_end:
    # While not at end, call nodes_map function for current position.
    for step in directions:
        path = nodes_map(current_pos)
        left = path[1]
        right = path[2]
        # If left then change current position to position's left mapping
        if step == 'L':
            current_pos = left
            print(current_pos)
        # If right then change current position to position's right mapping
        else:
            current_pos = right
            print(current_pos)
    # After each complete iteration of set of directions,
    # if current position is ZZZ then (number_interations * number steps in directions
    if current_pos == "ZZZ":
        at_end = True
        print(f"Number of steps to get to ZZZ: {number_iterations * len(directions)}")
    # if not at ZZZ repeat steps in directions
    else:
        number_iterations += 1
