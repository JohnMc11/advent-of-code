import re

file = open('input')
try:
    battery_bank_input = file.read()
finally:
    file.close()

battery_size = 12
total = 0
for line in battery_bank_input.splitlines():
    battery_cells = re.findall(r"""(\d)""", line, re.VERBOSE)

    battery = ""
    last_cell_index = -1
    for i in range(0, battery_size):
        cell_selection_slice_end = -(battery_size - 1 - i) if battery_size - 1 - i > 0 else None
        cell_selection = battery_cells[last_cell_index + 1:cell_selection_slice_end]
        cell_index = cell_selection.index(max(cell_selection)) + last_cell_index + 1
        last_cell_index = cell_index
        battery += str(battery_cells[cell_index])

    print(battery, end=" - ")
    print(len(battery))
    total += int(battery)

print("Total", total)