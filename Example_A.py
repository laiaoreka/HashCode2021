# Libraries:
import os

# Get current directory:
dir_path = os.path.dirname(os.path.realpath(__file__))

# Read input data files names from directory:
for root, directories, files in os.walk(dir_path, topdown=False):
    for name in sorted(files):
        if name.endswith(".in"):
            print(os.path.join(root, name))






