import os

dirname = os.path.dirname(__file__)
data_file_path = os.path.join(dirname, "..", "data", "data.csv")

with open(data_file_path) as file:
    for row in file:
        pass