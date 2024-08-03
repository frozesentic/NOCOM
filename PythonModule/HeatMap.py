import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict

# Define the log file path
log_file = r'C:\Users\creeh\OneDrive\Main\PROGRAMS\NOCOM\PythonModule\chunk_visits.txt'

# Read the chunk visit data
chunk_visits = defaultdict(int)
with open(log_file, 'r') as file:
    for line in file:
        x, z = map(int, line.strip().split())
        chunk_visits[(x, z)] += 1

# Define the range for the heatmap
range_x = (-100, 100)
range_z = (-100, 100)

# Initialize the heatmap data array
heatmap_data = np.zeros((range_x[1] - range_x[0] + 1, range_z[1] - range_z[0] + 1))

# Populate the heatmap data array with visit counts
for (x, z), count in chunk_visits.items():
    if range_x[0] <= x <= range_x[1] and range_z[0] <= z <= range_z[1]:
        heatmap_data[x - range_x[0], z - range_z[0]] = count

# Create the heatmap
plt.imshow(heatmap_data, cmap='hot', interpolation='nearest')
plt.colorbar(label='Chunk Visit Frequency')
plt.title('Chunk Visit Heatmap')
plt.xlabel('Chunk X')
plt.ylabel('Chunk Z')
plt.show()
