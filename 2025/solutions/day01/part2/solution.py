# Regex cheat sheet
# https://www.rexegg.com/regex-quickstart.php

import math
import re

file = open('input')
try:
    rotations_input = file.read()
finally:
    file.close()

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

    # preserve the current_pos as until we are done calculating how many times the rotation hits zero
    new_pos = (current_pos + rotate_count) % 100

    # calculate how many times the rotation will hit or land on zero
    full_rotations = int(rotate_count / 100)
    partial_rotation_count = rotate_count - full_rotations * 100

    # how many times the partial rotation wraps around zero
    partial_rotation_wrap = ((partial_rotation_count + current_pos > 100 or partial_rotation_count + current_pos < 0) and current_pos != 0)

    zero_count += abs(full_rotations) + partial_rotation_wrap + (new_pos == 0)

    # spin the dial to its new number and adjust it for the dial's range
    current_pos = new_pos

print("The password is", zero_count)