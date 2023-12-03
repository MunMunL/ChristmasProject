# --- Day 2: Cube Conundrum ---
# You're launched high into the atmosphere! The apex of your trajectory just barely reaches the surface of a large island floating in the sky. You gently land in a fluffy pile of leaves. It's quite cold, but you don't see much snow. An Elf runs over to greet you.
#
# The Elf explains that you've arrived at Snow Island and apologizes for the lack of snow. He'll be happy to explain the situation, but it's a bit of a walk, so you have some time. They don't get many visitors up here; would you like to play a game in the meantime?
#
# As you walk, the Elf shows you a small bag and some cubes which are either red, green, or blue. Each time you play this game, he will hide a secret number of cubes of each color in the bag, and your goal is to figure out information about the number of cubes.
#
# To get information, once a bag has been loaded with cubes, the Elf will reach into the bag, grab a handful of random cubes, show them to you, and then put them back in the bag. He'll do this a few times per game.
#
# You play several games and record the information from each game (your puzzle input). Each game is listed with its ID number (like the 11 in Game 11: ...) followed by a semicolon-separated list of subsets of cubes that were revealed from the bag (like 3 red, 5 green, 4 blue).
#
# For example, the record of a few games might look like this:
#
# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
# In game 1, three sets of cubes are revealed from the bag (and then put back again). The first set is 3 blue cubes and 4 red cubes; the second set is 1 red cube, 2 green cubes, and 6 blue cubes; the third set is only 2 green cubes.
#
# The Elf would first like to know which games would have been possible if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?
#
# In the example above, games 1, 2, and 5 would have been possible if the bag had been loaded with that configuration. However, game 3 would have been impossible because at one point the Elf showed you 20 red cubes at once; similarly, game 4 would also have been impossible because the Elf showed you 15 blue cubes at once. If you add up the IDs of the games that would have been possible, you get 8.
#
# Determine which games would have been possible if the bag had been loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes. What is the sum of the IDs of those games?

possible_game_id_list = []
game_red = 12
game_green = 13
game_blue = 14


with open("day_2_input.txt", mode="r") as input_file:
    all_games = [i.split(": ")[1] for i in input_file.read().strip().split("\n")]
print(all_games)

game_no = 1
for game in all_games:
    sub_game = [i.split(", ") for i in game.split("; ")]
    print(sub_game)

    max_red = 0
    max_green = 0
    max_blue = 0
    for colour in sub_game:
        for index in range (len(colour)):

            # print(colour[index].split())
            if (colour[index].split()[1]) == "red":
                red = int((colour[index].split()[0]))
                if red > max_red:
                    max_red = red
            elif (colour[index].split()[1]) == "green":
                green = int((colour[index].split()[0]))
                if green > max_green:
                    max_green = green
            elif (colour[index].split()[1]) == "blue":
                blue = int((colour[index].split()[0]))
                if blue > max_blue:
                    max_blue = blue

    print(max_red, max_green, max_blue)
    if max_red < game_red and max_green < game_green and max_blue < game_blue:
        possible_game_id_list.append(game_no)
    game_no += 1
print(possible_game_id_list)
print(sum(possible_game_id_list))


    # sub_game_colour = [j.split(" ") for j in sub_game]
    # print(sub_game_colour)
    # for k in range(6):
    #     sub_game_colour_dict = sub_game_colour[k](dict(zip(sub_game_colour[::2], sub_game_colour[1::2])))
    #     print(sub_game_colour_dict)




# print(all_games[0])
# print(len(all_games))

