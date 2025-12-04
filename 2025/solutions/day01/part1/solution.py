# Regex cheat sheet
# https://www.rexegg.com/regex-quickstart.php

import re

file = open('input')
rotations_input = file.read()

# use a regex pattern to match all rotations and capture the direction and the distance (or count)
regex_pattern = r"""\s*.*(?:([a-zA-Z])(\d+))+"""
regex = re.compile(regex_pattern, re.VERBOSE)

# get all rotations from the input using the regex pattern
rotation_matches = regex.findall(rotations_input)

current_pos = 50
zero_count = 0
for rotation in rotation_matches:
    direction : str = rotation[0].lower()
    rotate_count : int = int(rotation[1])

    # determine the direction and negate the rotation_count if the rotation is left
    if direction == 'l':
        rotate_count *= -1
    elif direction != 'r':
        raise ValueError("direction is an unexpected value")

    # spin the dial to its new number
    current_pos = (current_pos + rotate_count) % 100

    # check this after correcting for the dial range
    if current_pos == 0:
        zero_count += 1

print("The password is", zero_count)