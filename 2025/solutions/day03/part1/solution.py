import re

file = open('input')
try:
    battery_bank_input = file.read()
finally:
    file.close()

total = 0
for line in battery_bank_input.splitlines():
    battery_cells = re.findall(r"""(\d)""", line, re.VERBOSE)

    high_index = battery_cells.index(max(battery_cells[:-1]))
    second_high_index = battery_cells.index(max(battery_cells[high_index + 1:]))
    battery = str(battery_cells[high_index]) + str(battery_cells[second_high_index])

    total += int(battery)

print("Total", total)