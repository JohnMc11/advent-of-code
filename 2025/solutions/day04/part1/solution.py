import pandas as pd
import numpy as np

file = open('input')
try:
    grid_input = file.read()
finally:
    file.close()

# create a dataframe of individual characters (referred to as cells from this point forward)
df = pd.DataFrame(list(line) for line in grid_input.splitlines())
print(df)

stacked = df.stack()
for item in stacked:
    print(item)