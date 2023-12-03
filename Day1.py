# --- Day 1: Trebuchet?! ---
# Something is wrong with global snow production, and you've been selected to take a look.
# The Elves have even given you a map; on it,
# they've used stars to mark the top fifty locations that are likely to be having problems.
#
# You've been doing this long enough to know that to restore snow operations,
# you need to check all fifty stars by December 25th.
#
# Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar;
# the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!
#
# You try to ask why they can't just use a weather machine ("not powerful enough")
# and where they're even sending you ("the sky") and why your map looks mostly blank ("you sure ask a lot of questions")
# and hang on did you just say the sky ("of course, where do you think snow comes from") when you realize that the Elves
# are already loading you into a trebuchet ("please hold still, we need to strap you in").
#
# As they're making the final adjustments, they discover that their calibration document (your puzzle input)
# has been amended by a very young Elf who was apparently just excited to show off her art skills. Consequently,
# the Elves are having trouble reading the values on the document.
#
# The newly-improved calibration document consists of lines of text;
# each line originally contained a specific calibration value that the Elves now need to recover. On each line,
# the calibration value can be found by combining the first digit and the last digit (in that order)
# to form a single two-digit number.
#
# For example:
#
# 1abc2
# pqr3stu8vwx
# a1b2c3d4e5f
# treb7uchet
# In this example, the calibration values of these four lines are 12, 38, 15, and 77.
# Adding these together produces 142.
#
# Consider your entire calibration document. What is the sum of all of the calibration values?


codes_list = []
calibration_values_list = []
calibration_values_temp = 0
number_list_txt = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
num_char = []

# Extract provided input saved as .txt file
with open("day_1_input.txt", mode="r") as input_file:
    codes = input_file.readlines()

# Convert codes to a list
for code in codes:
    codes_list.append(code.strip())

# While loop for each item in code_list
i = 0
while i < len(codes_list):
    # For loop: for each character of code in question, add all identified numbers to num_char list to identify
    # first and last digit of the calibration value
    for code_char in codes_list[i]:
        if code_char in number_list_txt:
            num_char.append(code_char)
            first_digit = num_char[0]
            last_digit = num_char[-1]
            calibration_value = first_digit + last_digit
            calibration_values_temp = int(calibration_value)
    # Adds the calibration value to the calibration_values_list and reset num_char list for next code
    calibration_values_list.append(calibration_values_temp)
    num_char = []
    i += 1

print(sum(calibration_values_list))
